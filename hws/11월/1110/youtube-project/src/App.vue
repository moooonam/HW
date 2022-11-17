<template>
  <div id="app">
    <h1>My First Youtube Project</h1>
    <SearchTitle @give-to-title="appGetTitle" />
    <iframe
      id="ytplayer"
      type="text/html"
      width="720"
      height="405"
      :src="`https://www.youtube.com/embed/${this.id}`"
      frameborder="0"
      allowfullscreen="allowfullscreen"
    ></iframe>
    <br>
    <br>
    <iframe
      v-for="myid in getedData"
      :key="myid"
      id="ytplayer"
      type="text/html"
      width="200"
      height="100"
      :src="`https://www.youtube.com/embed/${myid.id.videoId}`"
      frameborder="0"
      allowfullscreen="allowfullscreen"
      style="margin: right 20px;"
    ></iframe>
  </div>
</template>

<script>
import SearchTitle from "@/components/SearchTitle";
import axios from "axios";

export default {
  name: "App",
  data() {
    return {
      id: null,
      // SRC:`https://www.youtube.com/embed/${this.id}`,
      getedData:null,
    };
  },
  components: {
    SearchTitle,
  },
  methods: {
    appGetTitle(inputData) {
      axios
        .get(
          `https://www.googleapis.com/youtube/v3/search?part=snippet&q=${inputData}&key=AIzaSyA4saGWPmhAPZBRV0Wf6_rkhrDTrLhPq0w
          &maxResults=10`
        )
        .then((response) => {
          console.log(response);
          this.getedData = response.data.items
          this.getedData.splice(1,1)
          this.id = response.data.items[0].id.videoId;
        });
    },
  },
};
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
