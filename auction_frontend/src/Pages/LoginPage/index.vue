
<template>


    <div class="container mt-5">
        <div class="row d-flex justify-content-center">
            <h1 class="mt-5 row d-flex justify-content-center">To proceed you must Login first</h1>
            <form @submit="submitedForm" class="row d-flex justify-content-center">
                <div class="col-md-6">
                    <div class="card px-5 py-5" id="login">
                        <div class="form-data" v-if="!submitted">

                            <div class="details-inputs mb-5"> <span>Email</span>
                                <input type="email" v-model="email" v-bind:class="{
                                    'form-control': true, 'is-invalid': formValidity.email
                                }" v-on:blur="validEmail(email);" id="email" placeholder="email">

                                <div class="invalid-feedback">Email is a mandatory field!</div>
                            </div>
                            <div class="details-inputs mb-5"> <span>Password</span>
                                <input type="password"
                                    v-bind:class="{ 'form-control': true, 'is-invalid': formValidity.password }"
                                    v-on:blur="(validPassword(password))" id="password" placeholder="password"
                                    v-model="password">
                                <div class="invalid-feedback">Password must contain at least 9 character!</div>
                            </div>
                            <div class="mb-5"> <button class="btn-dark btn  w-100" type="submit">Login</button></div>
                        </div>

                    </div>
                </div>
            </form>
        </div>
    </div>


</template>

<style scoped>
body {
    background: #000
}

h1 {
    color: #6B915B
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
    el: '#login',
    data: function () {
        return {
            email: "",
            submitted: false,
            password: "",
            formValidity: {
                email: false,
                password: false,
            }
        }
    },

    methods: {

        
        async submitedForm(e: { preventDefault: () => void; }) {
            
            e.preventDefault();
            const validatedEmail = this.validEmail(this.email);
            const validatedPassword = this.validPassword(this.password);

            console.log(validatedEmail)
            console.log(validatedPassword)
            if (validatedEmail || validatedPassword) return

            console.log("credentials work");
            try {
                const response = await fetch('http://127.0.0.1:8000/login/', {
                    method: 'POST',
                    body: JSON.stringify({
                        email: this.email,
                        password: this.password,
                    })
                    
                })

                let data = await response.json();

                console.log(data) // We are not getting ay token yet.

                // localStorage.setItem("django-token", data.token)

            } catch (e) {
                console.log("error occured", e)
            }

        },

        validEmail: function (email: string) {

            var regex_email = /^[_a-z0-9-+]+(\.[_a-z0-9-+]+)*(\+[a-z0-9-]+)?@[a-z0-9-.]+(\.[a-z0-9]+)$/;
            this.formValidity.email = !regex_email.test(email.toLowerCase());
            console.log(this.formValidity.email);
            return this.formValidity.email;

        },

        validPassword(password: string):boolean {
            this.formValidity.password = password.length <= 8;
            return this.formValidity.password;
        },




    }
}
</script>