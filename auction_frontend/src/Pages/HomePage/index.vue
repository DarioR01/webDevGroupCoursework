<script setup lang="ts">
import Item from '../../components/Item/index.vue'
</script>

<template>
  <h1 class="h1 mb-3 text-dark text-center">Open Bids</h1>
  <div class="container-xxl">
    <ul class="row row-cols-auto g-5 justify-content-md-center">
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
      <li class="col list-unstyled">
        <Item title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" endTime="Date in epoch" />
      </li>
    </ul>

  </div>
</template>
