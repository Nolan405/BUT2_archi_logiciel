<script>

import TodoItem from './components/TodoItem.vue';

let data = {
  todos: [{ text: 'Faire les courses', checked: true }, { text: 'Apprendre REST', checked: false }],
  title: 'Mes tâches',
  newItem: '',
  currentIndex: -1
};

export default {

  data() {
    return data;
  },
  methods: {
    addItem: function () {
      let text = this.newItem.trim();
      if (text) {
        this.todos.push({
          text: text,
          checked: false
        });
        this.newItem = '';
      }
    },
    suppItem: function (index) {
      this.todos.splice(index, 1);
    },
    modifItem: function (index) {
      this.currentIndex = index;
    },
    fermerModif: function () {
      this.currentIndex = -1;
    }
  },
  components: { TodoItem }
}
</script>


<template>
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
 <div  class="container">
<h2>{{ title }}</h2>
  <div v-if="currentIndex !== -1" class="alert">
    <input 
      type="text" 
      class="form-control" 
      v-model="todos[currentIndex].text"
      @keyup.enter="fermerModif"
    >
  </div>
  <ol>
    <todo-item 
        v-for="(todo, index) in todos" 
        :key="index" 
        :todo="todo"
        @remove="suppItem(index)"
        @modify="modifItem(index)"
      />
  </ol>
  <div class="input-group">
    <input v-model="newItem" 
     @keyup.enter="addItem" 
     placeholder="Ajouter une tache à la liste" 
    type="text"
    class="form-control">
    <span class="input-group-btn">
      <button @click="addItem" 
      class="btn btn-default" 
      type="button">Ajouter</button>
    </span>
  </div>
</div>
</template>
