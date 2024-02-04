<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Sheet from '@/components/Sheet.vue'


const showAssignment = ref(false)
const currSheet = ref({})

const statusStyles = (status) => {
      const colors = {
        assigned: { text: 'black', background: 'orange' },
        marked: { text: 'white', background: 'green' },
        unassigned: { text: "white", background: "grey" },
        assigning: { text: "black", background: "yellow" }
      };
      return colors[status]
    };

const back = () => {
  showAssignment.value = false
  currSheet.value = {}
}


const sheetAction = async (user) => {
  if (user.status == "unassigned") {
    for (let i = 0; i < users.value.length; i++) {
      console.log(users.value[i])
      if (users.value[i].name == user.name) {
        users.value[i].status = "assigning"
      }
    }

    const response = await fetch('http://127.0.0.1:5000/generate-sheet', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
      body: JSON.stringify({
        "name": user.name
      })
    });
    
    for (let i = 0; i < users.value.length; i++) {
      console.log(users.value[i])
      if (users.value[i].name == user.name) {
        users.value[i].status = "assigned"
      }
    }
  }else if (user.status == "assigned") {
    const response = await fetch('http://127.0.0.1:5000/get-assignment', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
      body: JSON.stringify({
        "name": user.name
      })
    });

    const sheet = await response.json()

    currSheet.value = sheet
    showAssignment.value = true
  }else if (user.status == "marked") {
    const response = await fetch('http://127.0.0.1:5000/get-assignment', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
      },
      body: JSON.stringify({
        "name": user.name
      })
    });

    const sheet = await response.json()

    currSheet.value = sheet.questions
    showAssignment.value = true
  }
}

const users = ref([])

const getStatuses = async () => {
  let newUsers = []
  const names = ["Ryan Doe", "Ashwin Doe", "Jane Doe"]

  for (name of names) {
      const response = await fetch('http://127.0.0.1:5000/assignment-status', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
        },
        body: JSON.stringify({
          "name": name
        })
      });

      const { status } = await response.json()
      newUsers.push({
        name,
        status
      })
  }

  users.value = newUsers
  console.log(users.value)
}

await getStatuses()
</script>

<template lang="pug">
.cards(v-if="!showAssignment") 
  .card(v-for="user in users"
    :key="user.name"
    :style="{ backgroundColor: statusStyles(user.status).background }" 
    @click="sheetAction(user)")

    h2 {{ user.name }}
    p.status(:style="{ color: statusStyles(user.status).text }") {{ user.status }}

div(v-if="showAssignment")
  button.button(@click="back()") Back
  br
  br
  Sheet(:questions="currSheet.questions")

</template>

<style lang="scss" scoped>
.button {
  background-color: #2ecc71;
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    cursor: pointer;
    margin-top: 1rem;
}
h2 {
  font-weight: 500;
  font-size: 20px;
  line-height: 24px;
}
.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  cursor: pointer;
  height: 15rem;
  width: 15rem;
  padding: 1rem;
  margin: 1rem;
  background: #fff;
  border-radius: 2px;
  overflow: hidden;
  
  position: relative;
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #888888;
  box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
  transition: all 0.2s ease-in-out;
  
  &:hover {
  box-shadow: 0 10px 20px rgba(0,0,0,0.19), 0 6px 6px rgba(0,0,0,0.23);
  
    .card-actions {
      transform: translateY(0);
      transition-timing-function:ease-out;
      transition-delay: 128ms;
    }
  }
}

.card-actions {
  position: absolute;
  background: rgba(0,0,0,.8);
  padding: 1rem;
  bottom: 0;
  left: 0;
  right: 0;
  top: 84px;
  transform: translateY(100%);
  transition: transform 128ms ease-in;
}

.btn {
  display: block;  
  padding: 6px 12px;
  margin-bottom: 12px;
  border-radius: 2px;
  
  font-size: 14px;
  line-height: 20px;
  text-align: Left;
  
  cursor: pointer;
  box-shadow: 0 1px 3px rgab(0,0,0,.24), 0 1px 2px rgab(0,0,0,.12);
  opacity: 0;
  transition: opacity 200ms ease-out,
              transform 200ms ease-out;
  transform: translateY(2rem);
}

.card:hover {
  
  .btn {
    opacity: 1;
    transform: translateY(0);
    
    &:first-child {
    transition-delay: 100ms;
    }
    &:nth-child(2) {
      transition-delay: 150ms;
    }
    &:nth-child(3) {
      transition-delay: 200ms;
    }
    &:nth-child(4) {
      transition-delay: 250ms;
    }
  }
}

.btn.primary {
  background: #3B98D3;
  color: white;
}

.btn.default {
  background: #F7F9F9;
}

.step-details {}
.step-type {  
  margin-bottom: 0.5rem;
  font-weight: bold;
}

.step-deadline {  
   // font-style: italic;
   color: #666;
}

.warning {
  color: orangered;
}
.error {
  color: #F00000;
}

i {
  width: 1rem;
  text-align: center;
  margin-right: .25rem;
}
.status {
    font-size: 0.75rem; // smaller text for status
    margin-top: 0.25rem; // space between the name and status
  }
</style>
