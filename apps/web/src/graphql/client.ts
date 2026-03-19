import { ApolloClient, InMemoryCache, HttpLink } from '@apollo/client';

const httpLink = new HttpLink({
  // Update this URI to match your Python API endpoint
  uri: import.meta.env.VITE_GRAPHQL_URL ?? 'http://localhost:8000/graphql',
});

/**
 * Apollo Client instance for GraphQL communication with the Python backend.
 * Wrap your app with <ApolloProvider client={apolloClient}> (already done in main.tsx).
 *
 * Usage:
 *   import { useQuery } from '@apollo/client';
 *   import { EXAMPLE_QUERY } from './queries';
 *   const { data, loading, error } = useQuery(EXAMPLE_QUERY);
 */
export const apolloClient = new ApolloClient({
  link: httpLink,
  cache: new InMemoryCache(),
});
