import { gql } from '@apollo/client';

/**
 * Example GraphQL query — replace with your actual queries.
 *
 * Usage with Apollo Client:
 *   import { useQuery } from '@apollo/client';
 *   const { data } = useQuery(PING_QUERY);
 */
export const PING_QUERY = gql`
  query Ping {
    ping
  }
`;
