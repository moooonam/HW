import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    counter: 0,
  },
  getters: {
    counterDouble(state){
      return state.counter*2
    },
  },
  mutations: {
    INCREASE(state, newCounter){
      state.counter = newCounter+1
    },
    DECREASE(state, newCounter){
      state.counter = newCounter-1
    },

  },
  actions: {
    increase(context, newCounter){
      context.commit('INCREASE', newCounter)
    },
    decrease(context, newCounter){
      context.commit('DECREASE', newCounter)
    }

  },
  modules: {
  }
})
