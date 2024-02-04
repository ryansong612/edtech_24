<template lang="pug">
.home-page
  .intro-section
      h1 Hi, this is quizGPT,
      p create computing problem sheets tailored to every coding learner in your class.
  .generator-form
    .form-group
      label(for="themes") Themes
      select#themes
        option(:value="theme") Select a theme
        // Add more theme options here
    .form-group
      label(for="number-of-questions") Number of questing
      input#number-of-questions(type="number" min="1")
    .form-group
      .difficulty-label Difficulties
      .difficulty-options
        .difficulty-option(v-for="difficulty in difficulties" :key="difficulty" :class="{ selected: selectedDifficulty === difficulty }" @click="selectDifficulty(difficulty)") {{ difficulty }}
    button.generate-btn(@click="generate") Generate
</template>
  
<script>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const difficulties = ['Easy', 'Medium', 'Hard', 'Insanely hard'];
    const selectedDifficulty = ref('Easy');
    const theme = ref('');
    const numberOfQuestions = ref(1);
    const router = useRouter();

    function selectDifficulty(difficulty) {
      selectedDifficulty.value = difficulty;
    }

    function generate() {
      // Trigger generation logic here
      console.log(theme.value);
      router.push({ name: 'Result', query: { theme: theme.value? theme.value : '(Theme)'}});
    }

    return {
      difficulties,
      selectedDifficulty,
      selectDifficulty,
      generate
    };
  }
};
</script>
  
<style lang="scss" scoped>
.home-page {
  height: 100vh;
  display: flex;
  flex-direction: row;
  align-items: center;
  color: white;
  padding: 2rem;

  .intro-section, .form-section {
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 2rem;
  }

  .generator-form {
    margin-top: 2rem;

    .form-group {
      margin-bottom: 1rem;
    }

    label {
      display: block;
    }

    select, input {
      width: 100%;
      padding: 0.5rem;
      margin-top: 0.5rem;
    }

    .difficulty-options {
      display: flex;
      justify-content: space-between;

      .difficulty-option {
        padding: 0.5rem 1rem;
        background-color: #7f8c8d; // Default background
        margin-right: 0.5rem;
        cursor: pointer;

        &:hover, &.selected {
          background-color: #27ae60; // Selected background
        }
      }
    }
  }

  .generate-btn {
    background-color: #2ecc71;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    margin-top: 1rem;

    &:hover {
      background-color: darken(#2ecc71, 10%);
    }
  }
}
</style>