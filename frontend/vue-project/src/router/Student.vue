<template lang="pug">
.home-page(v-if="!loggedIn")
  .intro-section
    h1 What's your name?
    input#input(v-model="name")
    button.assign-btn(@click="fetchSheet()") Go

.wrapper(v-if="loggedIn")
  .question-list
  StudentSheet(:questions="currSheet.questions")

</template>
    
<script setup>
import { ref } from "vue"
import StudentSheet from '@/components/StudentSheet.vue'

const name = ref("")
const loggedIn = ref(false)
const currSheet = ref([])

const fetchSheet = async () => {
  const response = await fetch('http://127.0.0.1:5000/get-assignment', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    body: JSON.stringify({
      "name": name.value
    })
  });

  const sheet = await response.json()
  currSheet.value = sheet
  loggedIn.value = true
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

  }
  
#input {
  background: none;
  border: none;
  border-bottom: white 1px solid;
  color: white
}

#input:focus {
  outline: none
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