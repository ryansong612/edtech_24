<!-- <template lang="pug">
.database-page
    .header
    h1 My database
    .search-bar
        input(type="search" placeholder="What are you looking for today?")
        button.filter Filter
        button.add +
    .content 123
    .entry(v-for="entry in entries" :key="entry.id")
        .question {{ entry.question }}
        .answer {{ entry.explanation }}
        button.show-more Show more
</template>
  
  <script>
  export default {
    setup() {
        const database = ref([]);
      return {
        entries: [
          // Replace with your actual data
          {
            id: 1,
            question: "Explain the purpose of the NumPy function np.save().",
            answer: "The np.save() function allows you to save NumPy arrays to disk. This is useful for persisting data between sessions.",
            type: "Short Answer",
          },
          // More entries...
        ]
      };
    }
  };
  </script>
  
  <style lang="scss" scoped>
  .database-page {
    .header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 1rem;
      background-color: #333;
      color: white;
  
      h1 {
        font-size: 2rem;
      }
  
      .search-bar {
        display: flex;
        align-items: center;
  
        input {
          padding: 0.5rem;
          margin-right: 0.5rem;
        }
  
        button {
          padding: 0.5rem 1rem;
          background-color: #2ecc71;
          border: none;
          color: white;
          cursor: pointer;
  
          &:hover {
            background-color: darken(#2ecc71, 10%);
          }
        }
  
        .add {
          font-size: 1.5rem;
          display: flex;
          align-items: center;
          justify-content: center;
          width: 2rem;
          height: 2rem;
          border-radius: 50%;
        }
      }
    }
  
    .content {
      .entry {
        background-color: #222;
        margin: 1rem;
        padding: 1rem;
        border-radius: 0.5rem;
        color: white;
  
        .question {
          font-weight: bold;
        }
  
        .code-snippet {
          background-color: #333;
          padding: 1rem;
          margin: 1rem 0;
          white-space: pre;
          overflow-x: auto;
        }
  
        .explanation {
          font-style: italic;
        }
  
        .show-more {
          background: none;
          border: none;
          color: #27ae60;
          cursor: pointer;
        }
      }
    }
  }
  </style>
   -->
   <template>
    1213
   </template>