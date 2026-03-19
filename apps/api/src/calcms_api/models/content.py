"""Content models for CRUD demonstration and early API development."""

from sqlmodel import Field, SQLModel


class ContentItemBase(SQLModel):
    title: str
    body: str
    published: bool = False


class ContentItem(ContentItemBase, table=True):
    __tablename__ = "content_items"

    id: int | None = Field(default=None, primary_key=True)


class ContentItemCreate(ContentItemBase):
    pass


class ContentItemRead(ContentItemBase):
    id: int


class ContentItemUpdate(SQLModel):
    title: str | None = None
    body: str | None = None
    published: bool | None = None