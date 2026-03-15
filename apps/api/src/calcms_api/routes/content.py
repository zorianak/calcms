from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from calcms_api.db import get_session
from calcms_api.models.content import (
    ContentItem,
    ContentItemCreate,
    ContentItemRead,
    ContentItemUpdate,
)

router = APIRouter(prefix="/content", tags=["content"])


@router.post("", response_model=ContentItemRead, status_code=status.HTTP_201_CREATED)
def create_content(payload: ContentItemCreate, session: Session = Depends(get_session)) -> ContentItem:
    item = ContentItem.model_validate(payload)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.get("", response_model=list[ContentItemRead])
def list_content(session: Session = Depends(get_session)) -> list[ContentItem]:
    return session.exec(select(ContentItem)).all()


@router.get("/{item_id}", response_model=ContentItemRead)
def get_content(item_id: int, session: Session = Depends(get_session)) -> ContentItem:
    item = session.get(ContentItem, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Content item not found")
    return item


@router.patch("/{item_id}", response_model=ContentItemRead)
def update_content(
    item_id: int,
    payload: ContentItemUpdate,
    session: Session = Depends(get_session),
) -> ContentItem:
    item = session.get(ContentItem, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Content item not found")

    updates = payload.model_dump(exclude_unset=True)
    for key, value in updates.items():
        setattr(item, key, value)

    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_content(item_id: int, session: Session = Depends(get_session)) -> None:
    item = session.get(ContentItem, item_id)
    if item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Content item not found")

    session.delete(item)
    session.commit()