<script lang="ts" setup >
import { getCookie } from '../../utility'
interface User {
  name: String;
  surname: String;
  email: String;
  date_of_first: Date;
}
</script>

<template>
  <div class="container mb-5">
    <div class="row">
      <div class="col-md-3">
        <div class="d-flex flex-column p-4 py-6 align-items-center text-center img_container"><img class="img-fluid"
            :src="`http://localhost:8000/static/${details.image_name}`">

          <span class="font-weight-bold">{{ details.name }}</span>
          <span class="text-black-50">{{ details.surname }}</span>
          <span class="text-black-50">{{ details.email }}</span>
          <span class="text-black-50">{{ details.date_of_birth }}</span>
         


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
              <div class="col-md-6"><label>Email</label><input type="text" class="form-control" v-model="email"
                  placeholder="Email">
              </div>
              <div class="col-md-6"><label>DOB</label>
                <input type="date" class="form-control" v-model="dob" placeholder="date of birth">
              </div>
              <div class="col-md-6"><label>Password</label>

              </div>

            </div>
            <div class="row mt-6">

            </div>
            <div class="mt-3"><button class="btn btn-primary profile-button" type="submit"> Save Profile </button></div>
          </div>
          <form @submit.prevent="updateImg">
            <input type="file" ref="file" @change="uploadFile" />
            <button class="btn btn-primary profile-button" type="submit">Upload Image</button>
          </form>
        </form>

      </div>
    </div>

  </div>

  <form class="form-outline" @submit.prevent="item">
    <div class="container align-items-center mt-5">
      <div class="row">
        <h4>Add Items</h4>
        <div class="row mt-2">
          <div class="col-md-3 mb-3"><input type="text" v-model="title" class="form-control" placeholder="title" />
          </div>
          <div class="col-md-3 mb-3 d-flex">
            <div ><input type="number" :min="1" v-model="price" class="form-control"
                placeholder="starting price">
            </div>
            <span class="h2">£</span>
          </div>
          <div class="mb-3">

            <label for="item">Bid End Date & Time:</label>
            <input type="datetime-local" v-model="end_date" id="item" name="birthday" />

          </div>

          <div class="col-md-6">
            <textarea class="form-control mb-3" v-model="description" placeholder="Add description" rows="3"></textarea>
          </div>


          <div class="mb-3">
            <input type="file" ref="itemFile" @change="uploadItemImg" />
          </div>

        </div>
        <div class="d-flex justify-content-between align-items-center mt-3">
          <button type="submit" class="btn btn-primary mb-5 btn-sm">Submit Item</button>
        </div>
      </div>
    </div>
  </form>









</template>
<style>
p {
  font-weight: bold;
}

.img-container {
  border: 1px solid
}
</style>

<script lang="ts" import datetime>
export default {
  data() {
    return {
      details: this.get_details(),
      name: "",
      surname: "",
      email: "",
      dob: "",
      file: "",
      title: "",
      price: "",
      end_date: "",
      item_image: "",
      description: "",
      $refs: {
        file: { files: [] },
        itemFile: { files: [] },
      }
    }
  },
  methods: {
    async get_details() {
      const response = await fetch("http://localhost:8000/bidder/api/profile/", {
        method: 'GET',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
      });
      const details = await response.json() as User;
      this.details = details;
    },
    async updateImg() {
      console.log("string")
      const formData = new FormData();
      formData.append('file', this.file as string);
      const headers = new Headers([['X-CSRFToken', getCookie('csrftoken')]]);
      const response = await fetch("http://localhost:8000/bidder/api/profile/", {
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
      const response = await fetch("http://localhost:8000/bidder/api/profile/", {
        method: 'PUT',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        headers,
        body: JSON.stringify({
          name: this.name,
          surname: this.surname,
          email: this.email,
          date_of_birth: date
        })
      });
      const details = await response.json() as User;
      this.details = details;
    },
    async item() {
      let date: Number = new Date(this.end_date).getTime();
      const headers = new Headers([['X-CSRFToken', getCookie('csrftoken')]]);
      const response = await fetch("http://localhost:8000/bidder/api/profile/", {
        method: 'POST',
        credentials: "include",
        mode: "cors",
        referrerPolicy: "no-referrer",
        headers,
        body: JSON.stringify({
          title: this.title,
          price: this.price,
          final_date: date,
          description: this.description
        })
      });
      if(response.status === 200){
        const data = await response.json()
        const id = data.id
        console.log(id)
        const formData = new FormData();
        formData.append('file', this.item_image);
        const secondResponse = await fetch(`http://localhost:8000/bidder/api/profile/${id}`, {
          method: 'POST',
          credentials: "include",
          mode: "cors",
          referrerPolicy: "no-referrer",
          headers,
          body: formData
        });

        this.title=""
        this.price=""
        this.end_date=""
        this.description=""
        this.item_image=""

        if(response.status === 200 && secondResponse.status === 200){
          alert("item successfully submitted")
        }
        else{
          alert("There has been an issue with the image file, and your item has been submitted without images")
        }
      }
      else{
        alert("Item could not be submitted, make sure your fields are correct")
      }
        
    },
    async uploadItemImg() {
      this.item_image = this.$refs.itemFile.files[0];
    },
  }
}
</script>