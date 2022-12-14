<script lang="ts" setup>
interface User {
  name: String;
  surname: String;
  email: String

}
</script>

<template>
  <div class="container mb-5">
    <div class="row">
      <div class="col-md-3">
        <div class="d-flex flex-column p-4 py-6 align-items-center text-center img_container"><img class=" mt-10"
            width="150px"
            src="https://st3.depositphotos.com/15648834/17930/v/600/depositphotos_179308454-stock-illustration-unknown-person-silhouette-glasses-profile.jpg">


        </div>
        <div>
          <span class="font-weight-bold">{{ details.name }}</span><span class="text-black-50">{{ details.surname
          }}</span><span><span class="text-black-50">{{ details.email }}</span>
          </span>
        </div>

      </div>


      <div class="col-md-5 border-right">
        <form class="form-outline" @submit.prevent="edit">

          <div class="p-3">
            <div class="d-flex justify-content-between align-items-center mb-3">
              <h4 class="text-right">Edit Profile</h4>
            </div>
            <div class="row mt-3">
              <div class="col-md-6"><label></label>
                <input type="text" class="form-control" placeholder="first name">
              </div>
              <div class="col-md-6"><label>Surname</label><input type="text" class="form-control" placeholder="surname">
              </div>
              <div class="col-md-6"><label>DOB</label>
                <input type="text" class="form-control" placeholder="date of birth">
              </div>

            </div>
            <div class="row mt-6">
              <div class="col-md-6">
                <label>Email </label>
                <input type="text" class="form-control" placeholder="enter email address" value="">
              </div>
            </div>
            <div class="mt-3"><button class="btn btn-primary profile-button" type="button"> Save Profile </button></div>
          </div>
        </form>
      </div>
    </div>

  </div>


  <div class="container align-items-center mt-5">
    <div class="row">
      <h4>Add Items</h4>
      <div class="row mt-2">
        <div class="col-md-3 mb-5"><input type="text" class="form-control" placeholder="title" /></div>
        <div class="col-md-3 mb-5"><input type="text" class="form-control" value="" placeholder="starting price"></div>
        <div>
          <form class="form-outline" @submit.prevent="item">
            <label for="item">Item end date</label>
            <input type="date" id="item" name="birthday">
          </form>
        </div>

      </div>
      <div class="col-md-6">
        <textarea class="form-control" placeholder="Add description" rows="3"></textarea>
      </div>
      <div class="d-flex justify-content-between align-items-center mt-3">
        <button type="submit" class="btn btn-primary btn-sm">Submit Item</button>
      </div>
    </div>
  </div>







  <div class="container py-5 ">
    <div class="row  d-flex justify-content-center ">
      <div class="col col-lg-9 col-xl-7">
        <div class="card">


          <div class="card-body p-4 text-black">
            <h4 class="text-right">Items Listed By You</h4>
            <div class="row g-2">
              <div class="col mb-2">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(112).webp" alt="item 1"
                  class="w-100 rounded-3">
                <p class="card-text justify-content-center">£100</p>
              </div>
              <div class="col mb-2">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(107).webp" alt="item 2"
                  class="w-100 rounded-3">
                <p class="card-text justify-content-center">£100</p>
              </div>
            </div>
            <div class="row g-2">
              <div class="col">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(108).webp" alt="item 3"
                  class="w-100 rounded-3">
                <p class="card-text justify-content-center">£200</p>
              </div>
              <div class="col">
                <img src="https://mdbcdn.b-cdn.net/img/Photos/Lightbox/Original/img%20(114).webp" alt="item 4"
                  class="w-100 rounded-3">
                <p class="card-text justify-content-center">£1K</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>



</template>
<style>
p {
  font-weight: bold;
}

.img-container {
  border: 1px solid
}
</style>

<script lang="ts">
export default {
  data() {
    return {
      details: this.get_details()

    }
  },

  methods: {


    async get_details() {
      const response = await fetch("http://localhost:8000/api/profile", {
        method: 'GET',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      const details = await response.json();
      this.details = details;
    },

    async edit() {
      const response = await fetch(`http://localhost:8000/api/edit_user}`, {
        method: 'POST',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
    },

    async item() {
      return
    }
  }
}
</script>