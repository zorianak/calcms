import { css } from '../styled-system/css';

function App() {
  return (
    <div className={css({ minH: '100vh', bg: 'white' })}>
      <main className={css({ p: '4' })}>
        <h1 className={css({ fontSize: '2xl', fontWeight: 'bold' })}>Welcome to CalCMS</h1>
      </main>
    </div>
  );
}

export default App;
