<script setup lang="ts">
import Item from '../../components/Item/index.vue'
</script>

<template>
  <h1 class="h1 mb-3 text-dark text-center">Open Bids</h1>
  <div class="container-xxl">
    <form @submit.prevent="getFilter" class=" row row-cols-auto justify-content-md-center mb-4">
      <input type="text" class="form-control mb-2" placeholder="Search" v-model="filter" />
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
      items: this.getItems(),
      filter: ""
    }
  },

  methods: {
    async getItems() {
      const response = await fetch(`http://localhost:8000/home/`, {
        method: 'GET',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      const itemsObject = await response.json();
      const items = Object.values(itemsObject);
      this.items = items;
    },

    async getFilter() {
      console.log(this.filter)
      const response = await fetch(`http://localhost:8000/home/?filter=${this.filter}`, {
        method: 'GET',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      const itemsObject = await response.json();
      const items = Object.values(itemsObject);
      this.items = items;
    }
  }
}
</script>
