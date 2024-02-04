<script>
import Question from '@/components/Questions.vue'; 
import { ref, computed, defineComponent, onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default defineComponent({
  components: {
    Question,
  },
  props: {
    userText: String
  },
  setup() {
    const questionsData = ref([]);
    const fetchQuestions = async () => {
      try {
        console.log("fetching");
        const response = await fetch('http://127.0.0.1:5000/get-questions', {
          method: 'POST',
          headers: {
            "Content-Type": "application/json; charset=UTF-8",
          }
        });
        const data = await response.json();
        let qs = []
        for (var i = 0; i < data['questions'].length; i++) {
          qs.push({'question': data['questions'][i]['question'],
                   'answer': data['questions'][i]['answer'],
                   'type': 'Short Answer'});
        }
        console.log(qs);
        questionsData.value = qs;
      } catch (error) {
        console.error('Failed to fetch questions:', error);
      }
    };

    onMounted(fetchQuestions);
    const students = ref([
      {
        name: 'Ryan Song',
        questions: questionsData
      }
    ]);
    
    const textarea = ref('');
    const route = useRoute();
    const router = useRouter();
    const theme = route.query.theme;

    const currentStudentIndex = ref(0);
    const currentStudent = computed(() => students.value[currentStudentIndex.value]);

    const saveAndAssign = () => {
      // TODO: backend add to database

      router.push({ name: 'Class' });
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
      length: students.value.length,
    };
  },
});
</script>


<template lang="pug">
.sticky
  .title
    | Assigning 
    span(style="text-decoration: underline;") {{theme}} 
    |  coursework for 
  .second
    .user-card
      .user-name {{ currentStudent.name }}
    .progress-bar
      // Component or HTML for the progress bar goes here

    button.download(@click="saveAndAssign") Save sheet and assigned
.wrapper
  button.navigation(@click="previousStudent" :class="{ 'disabled': currentStudentIndex === 0 }") Previous
  button.navigation.right(@click="nextStudent" :class="{ 'disabled': currentStudentIndex === length - 1 }") Next

  .question-list
    Question(:questions="currentStudent.questions", :status="currentStudent.status")

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
      font-size: 2rem;
      margin-right: 2rem;
      color: white;
    }

    .user-info {
      display: flex;

      .average, .assigned, .progress {
        margin-right: 2rem;
      }
    }
  }

button {
  padding: 1rem 1.5rem;
  margin-right: 1rem;
  border: none;
  border-radius: 0.3rem;
  cursor: pointer;
  font-size: 1.2em;
    background-color: #3b7d56; // Blue background color
    color: white;
    font-weight: bold;
}

.wrapper {
  position: relative;
}
.question-list {
  margin: 0 8em;
}
.navigation {
  position: sticky;
  top: 60%;
  background-color: #3b7d56; // Blue background color
  color: white;
  font-weight: bold;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.3rem;
  cursor: pointer;
  &.disabled {
    background-color: #555; // Darker color for disabled state
    cursor: not-allowed;
  }
}
.right {
  left: 100em;
} 
</style>