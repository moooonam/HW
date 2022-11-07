
<template>
  <div id="app">
    <p>Counter: {{ counter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  // data() {
  //   return {
  //     mycounter: 0,
  //   }
  // },
  methods: {
    increase() {
      const newCounter = this.$store.state.counter
      this.$store.dispatch('increase', newCounter)
    },
    decrease() {
      const newCounter = this.$store.state.counter 
      this.$store.dispatch('decrease', newCounter)
    },
  },
  computed: {
    // counterDouble: function () {
    //   return this.counter * 2
    // },
    counterDouble(){
      return this.$store.getters.counterDouble
    },
    counter(){
      return this.$store.state.counter
    },
  },
}
</script>

<style>
</style>