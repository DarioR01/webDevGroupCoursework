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
                            <input type="text" placeholder="name" class="form-control" id="name" v-model="name">
                            <label for="name">Name</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <div class="form-floating mb-3">
                            <input type="text" placeholder="surname" class="form-control" id="surname"
                                v-model="surname">
                            <label for="surname">Surname</label>
                        </div>
                    </div>
                </div>

                <div class="form-floating mb-3">
                    <input type="email" class="form-control" id="email" placeholder="email" v-model="email">
                    <label for="email">Email address</label>
                </div>

                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="password" placeholder="password" v-model="password">
                    <label for="password">Password</label>
                </div>

                <div class="input-group row g-2">
                    <div class="col-md">
                        <div class="form-floating">
                            <input type="tel" maxlength="2" placeholder="Day" class="form-control form-control-sm"
                                id="day" v-model="day" />
                            <label for="day">Day</label>
                        </div>
                    </div>
                    <div class="col-md">
                        <select class="form-select form-control" style="height: 3.625rem; padding: 1rem;"
                            v-model="month">
                            <option selected>Month</option>
                            <template v-for="month in months">
                                <option :value="month">{{ month }}</option>
                            </template>
                        </select>
                    </div>

                    <div class="col-md">
                        <div class="form-floating" id="year">
                            <input type="tel" maxlength="4" placeholder="Year" class="form-control" v-model="year" />
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
            name: undefined,
            surname: undefined,
            email: undefined,
            password: undefined,
            day: undefined,
            month: 'Month',
            year: undefined,
            months: ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        }
    },
    methods: {
        async formSubmit(e: { preventDefault: () => void; }) {
            e.preventDefault();
            const send_date: Number = Date.parse(`${this.day} ${this.month} ${this.year}`);

            try {
                const new_user = await fetch('https://localhost:8000/', {
                    method: 'POST', body: JSON.stringify({
                        name: this.name,
                        surname: this.surname,
                        email: this.email,
                        password: this.password,
                        date_of_birth: send_date,
                    })
                });
                location.replace('/login')
            } catch (e) {
                console.log("handle error")
            }

        }
    }
}
</script>