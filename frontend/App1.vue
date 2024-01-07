<template>
    <div id="app">
      <header>
        <h1>T.O.P 10 movies/videos</h1>
      </header>
      <main>
        <RankingComponent :items="popularItems" />
      </main>
      <footer>
        <p>DB_final_project</p>
      </footer>
    </div>
  </template>
  
  <script>
  import RankingComponent from './components/RankingComponent.vue';
  
  export default {
    name: 'App',
    components: {
      RankingComponent
    },
    data() {
      return {
        popularItems: [
          { id: 1, name: 'Item 1', avg_score: 5.0 },
          { id: 2, name: 'Item 2', avg_score: 4.8 },
          { id: 3, name: 'Item 3', avg_score: 4.7 },
          { id: 4, name: 'Item 4', avg_score: 4.6 },
          { id: 5, name: 'Item 5', avg_score: 4.5 },
          { id: 6, name: 'Item 6', avg_score: 4.4 },
          { id: 7, name: 'Item 7', avg_score: 4.3 },
          { id: 8, name: 'Item 8', avg_score: 4.2 },
          { id: 9, name: 'Item 9', avg_score: 4.1 },
          { id: 10, name: 'Item 10', avg_score: 4.0 },
          // Add more items with their scores
        ]
      };
    }
  };
  </script>
  
  <style>
  /* Global styles */
  body {
    margin: 0;
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    color: #333;
  }
  
  #app {
    max-width: 800px;
    margin: auto;
    padding: 20px;
  }
  
  header {
    background-color: #e26817;
    color: #fff;
    padding: 10px 0;
    text-align: center;
    border-top-left-radius: 8px;
    border-top-right-radius: 8px;
  }
  
  main {
    background: #fff;
    padding: 20px;
    border-bottom-left-radius: 8px;
    border-bottom-right-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  footer {
    text-align: center;
    padding: 10px 0;
    margin-top: 20px;
  }
  
  </style>
  