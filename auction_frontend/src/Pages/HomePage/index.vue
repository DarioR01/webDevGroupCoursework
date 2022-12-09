<script setup lang="ts">
import Item from '../../components/Item/index.vue'
</script>

<template>
  <h1 class="h1 mb-3 text-dark text-center">Open Bids</h1>
  <div class="container-xxl">
    <form class="row row-cols-auto justify-content-md-center mb-4">
      <input type="text" class="form-control mb-2" placeholder="Search" />
      <button type="submit" class="btn btn-primary">Search</button>
    </form>
    <ul class="row row-cols-auto g-5 justify-content-md-center">
      <li class="col list-unstyled" v-for="item in items">
        <Item :id="item.id" :title="item.title" :description="item.description" :price=item.price :time=item.time
          :image="item.img" />
      </li>
    </ul>

  </div>
</template>

<script lang="ts">
export default {
  data() {
    return {
      items: [
        { id: '1', title: 'Gold', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis tristique dui ac urna tincidunt, sit amet efficitur nulla maximus. Integer a lacus at magna porttitor', price: 2000, time: 1745668367000, img: 'https://picsum.photos/200/300' },
        { id: '2', title: 'Silver', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis tristique dui ac urna tincidunt, sit amet efficitur nulla maximus. Integer a lacus at magna porttitor Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis tristique dui ac urna tincidunt, sit amet efficitur nulla maximus. Integer a lacus at magna porttitor', price: 1000, time: 1864403827000, img: 'https://picsum.photos/200/300' },
        { id: '3', title: 'Incredible Toy', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', price: 30, time: 1787648469000, img: 'https://picsum.photos/200/300' },
        { id: '4', title: 'Underwear', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit.', price: 12, time: 1685414230000, img: 'https://picsum.photos/200/300' },
        { id: '5', title: 'Overwear', description: 'Lorem ipsum dolor sit amet.', price: 67, time: 1867158374000, img: 'https://picsum.photos/200/300' },
        { id: '6', title: 'Youwear', description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.', price: 1.56, time: 1781942194000, img: 'https://picsum.photos/200/300' }
      ]
    }
  }
}
</script>
