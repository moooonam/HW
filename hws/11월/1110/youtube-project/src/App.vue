<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchTitle
    @give-to-title="appGetTitle"
    />
  </div>
</template>

<script>
import SearchTitle from '@/components/SearchTitle'

export default {
  name: 'App',
  data(){
    return{
      
    }
  },
  components: {
    SearchTitle,
  },
  methods:{
    appGetTitle(inputData){
      console.log(inputData)

    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
