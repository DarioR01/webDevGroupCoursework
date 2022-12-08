<template>
  <router-link :style="{
    textDecoration: 'none', color: 'black'
  }" :to="{ name: 'Item', params: { id: id } }">
    <div class="card text-center" style="width: 18rem;">
      <img :src="image" class="card-img-top" alt="..." style="max-height: 12rem;">
      <div class="card-body">
        <h2 class="card-title">{{ title }}</h2>
        <p class="card-text">{{ description }}</p>
      </div>
      <div class="card-footer text-muted">
        <div class="card-subtitle mb-2 display-4">{{ price }}£</div>
        <span>ends on {{ (new Date(time)).getDay() }} {{ months[(new Date(time).getMonth())] }} {{ (new
            Date(time)).getFullYear()
        }}</span>
      </div>
    </div>
  </router-link>
</template>

<script lang="ts">
export default {
  props: {
    id: String,
    title: String,
    description: String,
    price: Number,
    time: { type: Number, default: Date.now() },
    image: String,
  },
  data() {
    return {
      months: [
        'January',
        'February',
        'March',
        'April',
        'May',
        'June',
        'July',
        'August',
        'September',
        'October',
        'November',
        'December'
      ],
    }
  }
}
</script>