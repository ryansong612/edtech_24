<template lang="pug">
.wrapper
  .question-container(v-for="(question, index) in questions" :key="index"
  :class="{ correctanswer: question.studentAnswer && question.studentAnswer === question.answer }")
    h2 Question {{ index + 1 }}: {{ question.question }}
    p.answer(v-if="question.type!= 'assigned' ") Student's Answer: 
        span(v-if="question.type !== 'MCQ'") {{ question.studentAnswer }}
        
    .mark(v-if="status === 'marked' ")
      ul.options(v-if="question.type === 'MCQ'")
        li(v-for="(choice, key) in question.choices" :key="key")
          label(:for="`question_${index}_${key}`")
          input(
            type="radio"
            :name="`question_${index}`"
            :id="`question_${index}_${key}`"
            :value="key"
            :checked="question.studentAnswer && question.choices[question.studentAnswer] === choice")
          span {{ key }}) {{ choice }}

      p.answer Answer: {{ question.answer }} 
      //- p.answer(v-if="status === 'marked'") Answer: {{ (question.answer + ": " + question.choices[question.answer])? question.type === 'MCQ': question.answer }} 
    
    .unmarked(v-if="status === 'unmarked' ")
      ul.options(v-if="question.type === 'MCQ'")
        li(v-for="(choice, key) in question.choices" :key="key")
          label(:for="`question_${index}_${key}`")
          input(
            type="radio"
            :name="`question_${index}`"
            :id="`question_${index}_${key}`"
            :value="key")
          span {{ key }}) {{ choice }}
  </template>

<script>
import { ref } from 'vue';
import { useRoute } from 'vue-router';

export default {
  setup() {
    const route = useRoute();
    const username = route.query.username;
    const status = route.query.status;
    const questions = ref([{
          "question": "What is the capital of France?",
          "answer": "Paris",
          "type": "Short Answer"
      },
      {
          "question": "What is the largest planet in our Solar System?",
          "choices": {
              "A": "Earth",
              "B": "Jupiter",
              "C": "Mars",
              "D": "Venus" 
          },
          "studentAnswer": "A",
          "answer": "A",
          "type": "MCQ"
      },
      {
            "question": "What is the boiling point of water?",
            "answer": "100°C",
            "type": "Short Answer"
      },
      {
            "question": "What is the capital of France?",
            "answer": "Paris",
            "type": "Short Answer"
      },
      {
            "question": "What is the largest planet in our Solar System?",
            "choices": {
                "A": "Earth",
                "B": "Jupiter",
                "C": "Mars",
                "D": "Venus" 
            },
            "studentAnswer": "A",
            "answer": "B",
            "type": "MCQ"
      },
      {
            "question": "What is the boiling point of water?",
            "answer": "100°C",
            "type": "Short Answer"
      }]);
    // Now you can use userName and questions in your template

    return {
      questions,
      username,
      status
    };
  }
};
</script>

<style lang="scss" scoped>
.wrapper {
  padding: 2em;
}
.question-container {
    position: relative;
    border-radius: 1em;
    border: 1px solid #008055;
    color: white;
    padding: 1rem;
    margin-bottom: 1rem;

    h2 {
    font-size: 1.2rem;
    color: #ecf0f1;
    }

    .options {
    list-style-type: none;
    padding: 0;

    li {
        margin: 0.5rem 0;

        label {
        cursor: pointer;

        input {
            margin-right: 0.5rem;
        }
        }
    }
    }

    .answer {
    padding: 0.5rem;
    border-radius: 0.25rem;
    }

    .minus {
        position: absolute;
        right: 1.5em;
        top: calc(50% - 1em);
        display: block;
        width: 2em;
        height: 2em;
        border: 1px solid white;
        border-radius: 50%;
        text-align: center;
        cursor: pointer;
    }
}

.correctanswer {
    background-color: #019a5a30;
}

.add-question {
    text-align: center;
    font-size: 1.5em;
    cursor: pointer;
}
.detail-view {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: #4a4a4a;

  .section {
    margin-bottom: 1rem;

    h3 {
      color: #ecf0f1;
    }

    .options {
      display: flex;
      button.option {
        background-color: #7f8c8d;
        border: none;
        color: white;
        padding: 0.5rem 1rem;
        margin-right: 0.5rem;
        cursor: pointer;

        &:hover {
          background-color: #95a5a6;
        }

        &.selected {
          background-color: #27ae60!important;
        }
        
      }

      
    }
    .selected {
      // Selected option styles
      background-color: #27ae60!important; // For example, a green background for selected options
    }
  }

  .generate-button {
    padding: 0.5rem 1rem;
    background-color: #2ecc71;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 1em;

    &:hover {
      background-color: #2ecc71;
    }
  }
}
</style>
