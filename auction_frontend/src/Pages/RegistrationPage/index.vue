<script setup lang="ts">
</script>

<template>
    <div class="container w-50">
        <div class="card p-5">
            <h1 class="text-center mb-5">Registration</h1>
            <form @submit="formSubmit">
                <div class="row g-2">
                    <div class="col-md">
                        <div class="form-floating mb-3">
                            <input type="text" placeholder="name"
                                v-bind:class="{ 'form-control': true, 'is-invalid': formValidity.name }"
                                v-on:blur="(isValidName(name))" id="name" v-model="name">
                            <label for="name">Name</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <div class="form-floating mb-3">
                            <input type="text" placeholder="surname"
                                v-bind:class="{ 'form-control': true, 'is-invalid': formValidity.surname }"
                                v-on:blur="(isValidSurname(surname))" id="surname" v-model="surname">
                            <label for="surname">Surname</label>
                        </div>
                    </div>
                </div>

                <div class="form-floating mb-3">
                    <input type="email" v-model="email" v-bind:class="{
                        'form-control': true, 'is-invalid': formValidity.email
                    }" v-on:blur="isValidEmail(email);" id="email" placeholder="email">
                    <label for="email">Email address</label>
                </div>

                <div class="form-floating mb-3">
                    <input type="password" v-bind:class="{ 'form-control': true, 'is-invalid': formValidity.password }"
                        v-on:blur="(isValidPassword(password))" id="password" placeholder="password" v-model="password">
                    <label for="password">Password</label>
                </div>

                <div class="input-group row g-2">
                    <div class="col-md">
                        <div class="form-floating">
                            <input type="tel" maxlength="2" placeholder="Day"
                                v-bind:class="{ 'form-control': true, 'form-control-sm': true, 'is-invalid': formValidity.date }"
                                id="day" v-model="day" />
                            <label for="day">Day</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <select
                            v-bind:class="{ 'form-control': true, 'form-select': true, 'is-invalid': formValidity.date }"
                            style="height: 3.625rem; padding: 1rem;" v-model="month">
                            <option selected>Month</option>
                            <template v-for="month in months">
                                <option :value="month">{{ month }}</option>
                            </template>
                        </select>
                    </div>

                    <div class="col-md">
                        <div class="form-floating" id="year">
                            <input type="tel" maxlength="4" placeholder="Year"
                                v-bind:class="{ 'form-control': true, 'is-invalid': formValidity.date }"
                                v-model="year" />
                            <label for="year">Year</label>
                        </div>
                    </div>
                </div>
                <div id="emailHelp" class="form-text mb-5">Your date of birth</div>


                <div class="d-flex justify-content-center">
                    <button class="btn btn-primary btn-lg btn-block" type="submit">Register</button>
                </div>
                <div class="d-flex justify-content-center">
                    <a href="/login" class="link-primary">Sign in instead</a>
                </div>

            </form>
        </div>
    </div>


</template>

<script lang="ts">
export default {
    data() {
        return {
            name: '',
            surname: '',
            email: '',
            password: '',
            day: undefined,
            month: 'Month',
            year: undefined,
            months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            formValidity: {
                name: false,
                surname: false,
                email: false,
                password: false,
                date: false,
            }
        }
    },
    methods: {
        async formSubmit(e: { preventDefault: () => void; }): Promise<void> {
            e.preventDefault();
            const isValidEmail = this.isValidEmail(this.email);
            const isValidPassword = this.isValidPassword(this.password);
            const isValidName = this.isValidName(this.name);
            const isValidSurname = this.isValidSurname(this.surname);

            const send_date: number = Date.parse(`${this.day} ${this.month} ${this.year}`);
            if (isNaN(send_date)) {
                this.formValidity.date = true;
            }

            if (isValidEmail || isValidPassword || isValidName || isValidSurname || this.formValidity.date) return

            try {
                const new_user = await fetch('http://127.0.0.1:8000/register/', {
                    method: 'POST', body: JSON.stringify({
                        name: this.name,
                        surname: this.surname,
                        email: this.email,
                        password: this.password,
                        date_of_birth: send_date,
                    })
                });
                window.location.href = '/login';
            } catch (error) {
                console.log(error)
            }

        },

        isValidEmail(email: string):boolean {
            const regex_email = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            this.formValidity.email = !regex_email.test(email.toLowerCase());
            return this.formValidity.email;
        },

        isValidPassword(password: string):boolean {
            this.formValidity.password = password.length <= 8;
            return this.formValidity.password;
        },

        isValidName(name: string):boolean {
            this.formValidity.name = name.length <= 0;
            return this.formValidity.name;
        },

        isValidSurname(surname: string):boolean {
            this.formValidity.surname = surname.length <= 0;
            return this.formValidity.surname;
        },

    }
}
</script>