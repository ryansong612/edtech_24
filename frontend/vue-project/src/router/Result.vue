<script>
import Question from '@/components/Questions.vue'; 
import { ref, computed, defineComponent } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default defineComponent({
  components: {
    Question,
  },
  props: {
    userText: String
  },
  setup() {
    const questionsData = ref([
      {
          "question": "What is the capital of France?",
          "answer": "Paris",
          "type": "Short Answer"
      },
      {
          "question": "What is the largest planet in our Solar System?",
          "answer": {
              "A": "Earth",
              "B": "Jupiter",
              "C": "Mars",
              "D": "Venus" 
          },
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
            "answer": {
                "A": "Earth",
                "B": "Jupiter",
                "C": "Mars",
                "D": "Venus" 
            },
            "type": "MCQ"
      },
      {
            "question": "What is the boiling point of water?",
            "answer": "100°C",
            "type": "Short Answer"
      }
    ]);
    const students = ref([
      {
        name: 'Yechuan Li',
        questions: questionsData
      },
      {
        name: 'John Doe',
        questions: questionsData
      },
      // ... other students
    ]);
    const textarea = ref('');
    const route = useRoute();
    const router = useRouter();
    const theme = route.query.theme;

    const currentStudentIndex = ref(0);
    const currentStudent = computed(() => students.value[currentStudentIndex.value]);

    const saveAndAssign = () => {
      // Logic for saving and assigning
      if (textarea.value.trim() !== '') {
        router.push({ name: 'Result', params: { userText: textarea.value } });
      } else {
        // Handle empty input error
      }
    };

    const previousStudent = () => {
      if (currentStudentIndex.value > 0) {
        currentStudentIndex.value--;
      }
    };

    const nextStudent = () => {
      if (currentStudentIndex.value < students.value.length - 1) {
        currentStudentIndex.value++;
      }
    };

    return {
      currentStudent,
      previousStudent,
      textarea,
      theme,
      nextStudent,
      saveAndAssign,
    };
  },
  methods: {
    Save() {
        console.log('Save');
    },
  },
});
</script>


<template lang="pug">
.sticky
  .title Assigning coursework for (Themes)
  .second
    .user-card
      .user-name {{ currentStudent.name }}
    .progress-bar
      // Component or HTML for the progress bar goes here

    button.download(@click="saveAndAssign") Save sheet and assigned

  .question-list
    Question(:questions="currentStudent.questions", :status="currentStudent.status")

  .navigation
    button(@click="previousStudent") Previous
    button(@click="nextStudent") Next
</template>

<style scoped lang="scss">
.sticky {
  position: sticky;
  top: 0;
  z-index: 100;
  background-color: #4a4a4a;
  /* Blue background */
  margin-bottom: 2em;
  height: 25vh;
  padding: 2em;
}
.second {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}
  .title {
    font-size: 2rem;
    margin-bottom: 2em;
  }

  .user-card {
    display: flex;
    align-items: center;

    .user-name {
      font-size: 1.5rem;
      margin-right: 2rem;
    }

    .user-info {
      display: flex;

      .average, .assigned, .progress {
        margin-right: 2rem;
      }
    }
  }

    button {
      padding: 0.5rem 1rem;
      margin-right: 1rem;
      border: none;
      border-radius: 0.3rem;
      cursor: pointer;

        background-color: #3b7d56; // Blue background color
        color: white;
        font-weight: bold;
    }

</style>