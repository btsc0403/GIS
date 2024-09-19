<template>
  <div class="app-container">
    <!-- 左侧地图面板 -->
    <Mars2dMap class="map_container" :url="configUrl" map-key="test" @onload="marsOnload" />

    <!-- 右侧组件面板 -->
    <div class="right-panel">
      <Coordinatelist :coordinates="[]" class="coord_panel"></Coordinatelist>
      <Chatbox class="chat_panel"></Chatbox>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as mars2d from "mars2d"
import Mars2dMap from "./components/mars-work/mars2d-map.vue"
import sidepanel from "./components/mars-work/sidepanel.vue"
import Coordinatelist from "./components/mars-work/coordinatelist.vue"
import Chatbox from "./components/mars-work/chatbox.vue"
const configUrl = "config/config.json"

const marsOnload = (map: any) => {
  const graphicLayer = new mars2d.layer.GraphicLayer({})
  map.addLayer(graphicLayer)

  graphicLayer.on(mars2d.EventType.click, (event: any) => {
    console.log("监听layer，单击了矢量对象", event)
  })
}
</script>

<style scoped>
.app-container {
  display: flex;
  height: 100vh;
  width: 100vw;
}

.map_container {
  height: 100%;
  width: 70%; /* Map占据左侧70% */
  margin-right: 20px; /* 右侧与其他元素留一些间隙 */
  border-radius: 10px; /* 圆角 */
  border: 2px solid #00f; /* 蓝色边框 */
  box-shadow: 0 0 15px rgba(0, 0, 255, 0.5); /* 荧光效果 */
  overflow: hidden; /* 确保内部内容不会超出边框 */
}

.right-panel {
  display: flex;
  flex-direction: column;
  width: 30%; /* 右侧占据30% */
  gap: 20px; /* 元素之间的空隙 */
}

.coord_panel,
.chat_panel {
  flex: 1; /* 占据剩余空间的1/2 */
  border-radius: 10px; /* 圆角 */
  border: 2px solid #00f; /* 蓝色边框 */
  box-shadow: 0 0 15px rgba(0, 0, 255, 0.5); /* 荧光效果 */
  background-color: #f8f8ff; /* 给面板一个背景色 */
}
/* 地图容器的外层矩形框样式 */

</style>
