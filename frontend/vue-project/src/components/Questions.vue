<template lang="pug">
.question-container(v-for="(question, index) in questions" :key="index")
    h2 Question {{ index + 1 }}: {{ question.question }}
    ul.options(v-if="question.type === 'MCQ'")
        li(v-for="(choice, key) in question.choices" :key="key")
            label(:for="`question_${index}_${key}`")
            input(
              type="radio"
              :name="`question_${index}`"
              :id="`question_${index}_${key}`"
              :value="key"
              :checked="question.choices[question.answer] === choice")
            span {{ key }}) {{ choice }}
    p.answer(v-else) Answer: {{ question.answer }}

.question-container.detail-view(v-if="isDetailedView")
  .section.difficulties
    h3 Question
    input(v-model="newQuestion")
  .section.question-types
    h3 Answer
    input(v-model="newAnswer")
  button.generate-button(@click="addQuestion()") Add

.question-container.add-question(v-else @click="toggleView") + Add a new Question +
</template>
    
<script setup>
import { ref, defineProps } from 'vue';

const props = defineProps(["questions"])

const newQuestion = ref("")
const newAnswer = ref("")
const isDetailedView = ref(false);

const addQuestion = async () => {
  const questionJson = {
          "question": newQuestion.value,
          "answer": newAnswer.value,
          "type": "Short Answer"
        }
  const response = await fetch("http://127.0.0.1:5000/add-questions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json; charset=UTF-8"
    },
    body: JSON.stringify({
        "questions": [questionJson]
    })
  })

  props.questions.push(questionJson)
  toggleView()
}

const toggleView = () => {
  isDetailedView.value = !isDetailedView.value;
}

/*
export default {
    props: {
      questions: Array
    },
  setup() {
    const selectedDifficulty = ref('Easy');
    const selectedQuestionType = ref('MCQ');
    const selectedPurpose = ref('Reinforcement');
    const newQuestion = ref("asdsdadsadsa")
    const newAnswer = ref("")

    const difficulties = ['Easy', 'Medium', 'Hard'];
    const questionTypes = ['Options', 'Shortanswers'];
    const purposes = ['Reinforcement', 'New knowledge'];

    function toggleView() {
      isDetailedView.value = !isDetailedView.value;
    }
    const selectedStyle = {
      backgroundColor: '#27ae60', // Green background for selected options
      color: 'white' // White text for selected options
    };

    function selectDifficulty(difficulty) {
      selectedDifficulty.value = difficulty;
      console.log(selectedDifficulty.value);
    }

    function selectQuestionType(type) {
      selectedQuestionType.value = type;
    }

    function selectPurpose(purpose) {
      console.log(purpose);
      selectedPurpose.value = purpose;
    }

    return {
      isDetailedView,
      difficulties,
      questionTypes,
      purposes,
      selectDifficulty,
      selectQuestionType,
      selectPurpose,
      toggleView
    };
  },
    methods: {
        removeQuestion(index) {
        this.questions.splice(index, 1);
        },
        addQuestion() {
          console.log(newQuestion.value)
        }
  }
};
*/
</script>

<style lang="scss" scoped>
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
