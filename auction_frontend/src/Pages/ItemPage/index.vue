<script lang="ts" setup>
import { getCookie } from '../../utility'
interface Question {
    id?: number;
    item_id: number;
    question: string;
    answer?: string;
}

interface Item {
    id: number;
    title: string;
    description: string;
    price: number;
    questions: Array<Question>
}

</script>
<template>
    <div class="container">
        <div class="card mb-3">
            <div class="row g-0">

                <picture class="col-md-4">
                    <img src="http://localhost:8000/static/default.jpg" alt="Image depicting the item" />
                </picture>

                <div class="col-md-8">
                    <div class="card-body">
                        <h1 class="card-title">{{ item.title }}</h1>
                        <p class="card-text">{{ item.description }}</p>
                        <form class="form-outline" @submit="bid">
                            <span>
                                Current Bid:
                                <strong class="display-6">{{ item.price }}£</strong>
                            </span>
                            <input id="bid" class="form-control" style="max-width: 200px;" type="number"
                                :min="(item.price + 1)" v-model="new_price" />
                            <label for="bid">Enter £{{ item.price + 1 }} or higher</label>
                            <br />
                            <button type="submit" class="btn btn-primary btn-lg">Bid</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>



        <h2>Questions</h2>
        <ul class="list-group mb-1">
            <template v-for="question in questions">
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">{{ question.question }}</div>
                        <div v-if="item.answer !== ''">{{ question.answer }}</div>
                        <div v-else>
                            <form class="form-outline" @submit="answer">
                                <div class="d-flex align-items-center">
                                    <div class="form-floating mb-3">
                                        <input type="email" class="form-control" id="answerQuestion">
                                        <label for="answerQuestion">Click to Answer the question</label>
                                    </div>
                                    <div>
                                        <button type="submit" class="btn btn-primary">Answer</button>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>
                </li>
            </template>
        </ul>
        <form class="form-outline" @submit="ask">
            <div class="form-floating">
                <input type="text" class="form-control" id="askQuestion" v-model="new_question">
                <label for="askQuestion">Click to ask a question</label>
            </div>
            <br />
            <button type="submit" class="btn btn-primary btn-lg">ask</button>
        </form>


        <form class="form-outline" @submit="answer">
            <div class="d-flex align-items-center">
                <div class="form-floating mb-3">
                    <input type="file" class="form-control" id="answerQuestion" @change="uploadFile" ref="file">
                </div>
                <div>
                    <button type="submit" class="btn btn-primary">Answer</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script lang="ts">
export default {
    data() {
        return {
            item: this.getItems(),
            questions: [] as Array<Question>,
            new_price: 0,
            new_question: "",
            file: {},
        }
    },

    methods: {
        async getItems() {
            const response = await fetch(`http://localhost:8000/item/${this.$route.params.id}`, {
                method: 'GET',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
            });
            const item = await response.json();
            console.log(item);
            this.item = item;
            const questions: Array<Question> = Object.values(item.questions);
            this.questions = questions;
        },

        async bid(e: { preventDefault: () => void; }) {
            e.preventDefault();
            if (this.item.price < this.new_price) {
                const response = await fetch(`http://localhost:8000/item/${this.$route.params.id}`, {
                    method: 'PUT',
                    credentials: "include",
                    mode: "cors",
                    contentType: 'multipart/form-data',
                    referrerPolicy: "no-referrer",
                    headers: { 'X-CSRFToken': getCookie('csrftoken') },
                    body: JSON.stringify({
                        price: this.new_price
                    })
                });
                console.log(response)
                if (response.status === 200) {
                    this.item.price = this.new_price
                }
                else {
                    window.alert("Your bid was not successful");
                }
            }
            else {
                window.alert("Your price was lower than the current bid");
            }
        },

        async ask(e: { preventDefault: () => void; }) {
            e.preventDefault();
            if (this.new_question != null) {
                const response = await fetch(`http://localhost:8000/item/${this.$route.params.id}`, {
                    method: 'POST',
                    credentials: "include",
                    mode: "cors",
                    referrerPolicy: "no-referrer",
                    headers: { 'X-CSRFToken': getCookie('csrftoken') },
                    body: JSON.stringify({
                        question: this.new_question
                    })
                });
                if (response.status === 200) {
                    this.questions.push({ item_id: this.item.id, question: this.new_question })
                }
                else {
                    window.alert("You bid was not successful");
                }
            }
            else {
                window.alert("question cannot have an empty body");
            }
        },

        uploadFile() {
            this.file = this.$refs.file.files[0];
        },

        async answer(e: { preventDefault: () => void; }) {
            e.preventDefault();
            const formData = new FormData();
            formData.append('file', this.file);

            for (var key of formData.entries()) {
                console.log(key[0] + ', ' + key[1]);
            }
            const response = await fetch(`http://localhost:8000/image/`, {
                method: 'POST',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: formData,
            });
            console.log(response)
        },
    }
}
</script>