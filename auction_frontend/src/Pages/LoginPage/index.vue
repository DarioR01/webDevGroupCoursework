
<template>


    <div class="container mt-5">
    <div class="row d-flex justify-content-center">
        <h1 class="mt-5 row d-flex justify-content-center">To proceed you must Login first</h1>
        <div class="col-md-6">
            <div class="card px-5 py-5" id="form1">
                <div class="form-data" v-if="!submitted">
                    <div class="details-inputs mb-5"> <span>Email</span> <input autocomplete="off" type="text" v-model="email" v-bind:class="{'form-control':true, 'is-invalid' : !validEmail(email) && BlurEmail}" v-on:blur="BlurEmail = true">
                        <div class="invalid-feedback">Email is a mandatory field!</div>
                    </div>
                    <div class="details-inputs mb-5"> <span>Password</span> <input autocomplete="off" type="password" v-model="password" v-bind:class="{'form-control':true, 'is-invalid' : !validPassword(password) && BlurPassword}" v-on:blur="BlurPassword = true">
                        <div class="invalid-feedback">Password must contain at least 9 character!</div>
                    </div>
                    <div class="mb-5"> <button class="btn-dark btn  w-100">Login</button></div>
                </div>

            </div>
        </div>
    </div>
</div>


</template>

<style scoped>
body {
    background: #000
}
h1{
    color:#6B915B
}
.container {
    border: 2px solid #2C2C2C;

}

h1 {
    margin-top: 70px
}

.card {
    border: none;
    height: 400px
}

.details-inputs {
    position: relative
}

.details-inputs span {
    position: absolute;
    top: -18px;
    left: 10px;
    background-color: #fff;
    padding: 5px 10px;
    font-size: 15px
}

.details-inputs input {
    height: 50px;
    width: 550px;
    border: 2px solid #eee
}

.details-inputs input:focus {
    box-shadow: none;
    outline: none;
    border: 2px solid #000
}

.btn {
    height: 50px
}


</style>

<script lang="ts">
export default {
    el: '#form1',
    data: function () {
        return {
            email: "",
            valid: false,
            submitted: false,
            password: "",
            BlurEmail: false,
            BlurPassword: false
        }
    },

    methods: {

        validate: function () {
            
            this.BlurPassword = true;
            
            if (this.validEmail(this.email) && this.validPassword(this.password)) {
                this.valid = true;
            }
        },

        validEmail: function (email:any) {

            var regex_email = /^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9!?@#$%^&*()_]+){8,20}$"/;
            if (regex_email.test(email.toLowerCase())) {
                return true;
            }

        },

        validPassword: function (password: any) {
            if (password.length > 8) {
                return true;
            }
        },

    }
}
</script>