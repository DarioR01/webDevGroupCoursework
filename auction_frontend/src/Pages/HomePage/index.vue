<script setup lang="ts">
import Item from '../../components/Item/index.vue'
</script>

<template>
  <h1 class="h1 mb-3 text-dark text-center">Open Bids</h1>
  <div class="container-xxl">
    <ul class="row row-cols-auto g-5 justify-content-md-center">
      <li class="col list-unstyled">
        <Item id="1" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="2" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="3" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="4" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="5" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="6" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
      <li class="col list-unstyled">
        <Item id="7" title="Gold" description="A bar of gold worth a lot" :price=16 :time=1668826865000
          image="https://picsum.photos/200/300" />
      </li>
    </ul>

  </div>
</template>
