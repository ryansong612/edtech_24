<template lang="pug">
.home-page
  .intro-section
      h1 Hi, this is quizGPT,
      p creating problem sheets tailored to every learner in your class.
  .generator-form
    .form-group
      label(for="themes") Themes
      select#themes(v-model="selectedTheme")
        option(:value="themes") Select a theme
        option(v-for="theme in themes" :value="theme" :key="theme") {{ theme }}
    .form-group
      label(for="number-of-questions") Number of questions
      input#number-of-questions(type="number" min="1" v-model="numberOfQuestions")
    button.generate-btn(@click="requestSheet()") Generate

.wrapper
  .question-list
    Sheet(:questions="currSheet.questions")

center
  button.assign-btn(@click="assignSheet()", v-if="currSheet.questions") Assign
</template>
  
<script setup>
import { ref } from 'vue';
import Sheet from '@/components/Sheet.vue'; 

const themes = [
      "Object Oriented Programming", "Functional Programming", "Data Structures", "Algorithms",
      "Operating Systems", "Compilers", "Databases",
      "Web Development", "Machine Learning", "Networks and Communication",
      "Natural Language Processing", "Reinforcement Learning", "Robotics",
      "Deep Learning", "Mathematics and Computer Science"
    ];

const selectedTheme = ref("")
const numberOfQuestions = ref(1)
const currSheet = ref({})

const requestSheet = async () => {
  const topK = Number(numberOfQuestions.value)
  const tag = selectedTheme.value

  const response = await fetch('http://127.0.0.1:5000/generate-questions', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      "tag": tag,
      "top_k": topK
    })
  });

  const sheet = await response.json();
  currSheet.value = sheet
}

const assignSheet = async () => {
  const response = await fetch('http://127.0.0.1:5000/assign-to', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      "name": "Ryan Doe",
      "questions": currSheet.value.questions
    })
  });

  const data = await response.json()

  if (data.status != "success") {
    alert("shit bro")
  }
}
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

.assign-btn {
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

.wrapper {
  position: relative;
}
.question-list {
  margin: 0 8em;
}
</style>