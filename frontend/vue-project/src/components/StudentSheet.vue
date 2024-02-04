<template lang="pug">
div(v-if="!done")
    br
    h2 Question {{ currIndex + 1 }}
    br
    p {{ questions[currIndex].question }}
    br
    textarea#answer-box(v-if="questions[currIndex].type == 'Short Answer'", v-model="userAnswers[currIndex]['user-answer']")
    br
    ul.options(v-if="questions[currIndex].type === 'MCQ'")
                li(v-for="(choice, key) in question.choices" :key="key")
                    label(:for="`question_${index}_${key}`")
                    input(
                    type="radio"
                    :name="`question_${index}`"
                    :id="`question_${index}_${key}`"
                    :value="key"
                    :checked="question.choices[question.answer] === choice")
                    span {{ key }} {{ choice }}
    br
    button.btn(@click="prevQuestion()", v-if="currIndex > 0") Back
    button.btn(@click="nextQuestion()", v-if="currIndex < questions.length - 1") Next
    button.btn(@click="submit()") Submit

div(v-if="done")
    .question-container(v-for="(question, index) in userAnswers" :key="index")
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
        div(v-else)
            p.answer Your Answer :: {{ question["user-answer"] }}
            p.answer Correct Answer: {{ question.answer }}
    
</template>
            
<script setup>
import { ref, defineProps } from 'vue';
        
const props = defineProps(["questions"])
const currIndex = ref(0)
const userAnswers = ref(props.questions.map((question) => {
    return {
        "question": question.question,
        "answer": question.answer,
        "user-answer": ""
    }
}))
const done = ref(false)

const nextQuestion = () => {
    currIndex.value += 1
    console.log(userAnswers.value)
}

const prevQuestion = () => {
    currIndex.value -= 1
}

const submit = async () => {
   const response = await fetch('http://127.0.0.1:5000/mark-sheet', {
        method: 'POST',
        headers: {
        "Content-Type": "application/json; charset=UTF-8",
        },
        body: JSON.stringify(userAnswers.value)
    });

    const marked = await response.json()

    for (let i = 0; i < marked.questions.length; i++) {
        userAnswers.value[i].status = marked.questions[i].status
    }
}
</script>
        
<style lang="scss" scoped>
h2, p {
    color: white
}

.btn {
  background-color: #2ecc71;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-top: 1rem;
  margin-right: 1rem;

  &:hover {
    background-color: darken(#2ecc71, 10%);
  }
}

#answer-box {
    width: 20rem;
    height: 5rem;
    &:focus {
        outline: none
    }
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
</style>
        