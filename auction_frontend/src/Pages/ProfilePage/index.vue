
<script lang="ts" setup>
import { getCookie } from '../../utility'
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
        <div class="d-flex flex-column p-4 py-6 align-items-center text-center img_container"><img class="img-fluid"
            :src="`http://localhost:8000/static/${details.image_name}`">


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
              <div class="col-md-6"><label>Name</label>
                <input type="text" class="form-control" v-model="name" placeholder="first name">
              </div>
              <div class="col-md-6"><label>Surname</label><input type="text" class="form-control" v-model="surname"
                  placeholder="surname">
              </div>
              <div class="col-md-6"><label>DOB</label>
                <input type="date" class="form-control" v-model="dob" placeholder="date of birth">
              </div>
              <div class="col-md-6"><label>Password</label>
                <!-- <input type="password" v-model="password" class="form-control" placeholder="password"> -->
              </div>

            </div>
            <div class="row mt-6">

            </div>
            <div class="mt-3"><button class="btn btn-primary profile-button" type="submit"> Save Profile </button></div>
          </div>
        </form>
        <form @submit.prevent="updateImg">
          <input type="file" ref="file" @change="uploadFile" />
          <button class="btn btn-primary profile-button" type="submit">Upload Image</button>
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
      details: this.get_details(),
      name: "",
      surname: "",
      dob: "",
      // password: "",
      file: {},
    }
  },

  methods: {


    async get_details() {
      const response = await fetch("http://localhost:8000/api/profile/", {
        method: 'GET',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      const details = await response.json();
      this.details = details;
    },

    async updateImg() {
      console.log("string")
      const formData = new FormData();
      formData.append('file', this.file);
      const headers = new Headers([['X-CSRFToken', getCookie('csrftoken')]]);
      const response = await fetch("http://localhost:8000/api/profile/", {
        method: 'POST',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        headers,
        body: formData
      });
      const image = await response.json();
      this.details.image_name = image.image
    },

    async uploadFile() {

      this.file = this.$refs.file.files[0];
    },




    async edit() {
      const date: Number = Date.parse(this.dob)
      const headers = new Headers([['X-CSRFToken', getCookie('csrftoken')]]);
      const response = await fetch("http://localhost:8000/api/profile", {
        method: 'PUT',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        headers,
        body: JSON.stringify({
          name: this.name,
          surname: this.surname,
          date_of_birth: date

        })
      });
    },


    async item() {
      return
    }
  }
}
</script>