<script>

export default{
    props: {
        todo : Object
    },
    methods:{
        suppr : function() {
            this.$emit('remove',{id:this.todo.id});
        },
        modif : function() {
            this.$emit('modify',{id:this.todo.id});
        }
    },
    emits: ['remove', 'modify']
}
</script>

<template>
    <li :class="{ 'alert alert-success': todo.checked }">
        <div class="checkbox">
            <label>
                <input type="checkbox" v-model="todo.checked"> 
                {{ todo.text }}
            </label>
            <button @click=suppr class="btn btn-danger btn-sm">
                Supprimer
            </button>
            <button @click=modif class="btn btn-warning btn-sm">
                Modifier
            </button>
        </div>
    </li>
</template>

<style scoped>
li {
  list-style-position: inside;
}

.btn-danger, .btn-warning {
    margin-left: 1em;
}
</style>