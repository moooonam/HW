<template>
  <div>
		검색:
		<input type="text"
		v-model="inputData" @keyup.enter="giveToTitle">
	</div>
</template>

<script>
export default {
	name: 'SearchTitle',
	data (){
		return{
			inputData:null,
		}
	},
	methods:{
		giveToTitle(){
			this.$emit('give-to-title', this.inputData)
			
		}
	}
}
</script>

<style>

</style>