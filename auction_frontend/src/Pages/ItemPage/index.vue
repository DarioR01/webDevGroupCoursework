<script lang="ts" setup>
import { getCookie } from '../../utility'
interface Question {
    id?: string;
    item_id?: number;
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
                    <img class="img-fluid" :src="`http://localhost:8000/static/${item.image_name}`"
                        alt="Image depicting the item" />
                </picture>

                <div class="col-md-8">
                    <div class="card-body">
                        <h1 class="card-title">{{ item.title }}</h1>
                        <p class="card-text">{{ item.description }}</p>
                        <form class="form-outline" @submit.prevent="bid">
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
            <template v-for="question, index in questions">
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">{{ question.question }}</div>
                        <div v-if="question.answer !== '' && question.answer !== undefined">{{ question.answer }}</div>
                        <div v-else>
                            <form class="form-outline" @submit.prevent="answer(question.id, index)">
                                <div class="d-flex align-items-center">
                                    <div class="form-floating mb-3">
                                        <input type="text" class="form-control" :id="question.id"
                                            v-model="new_answer[index]">
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
        <form class="form-outline" @submit.prevent="ask">
            <div class="form-floating">
                <input type="text" class="form-control" id="askQuestion" v-model="new_question">
                <label for="askQuestion">Click to ask a question</label>
            </div>
            <br />
            <button type="submit" class="btn btn-primary btn-lg">ask</button>
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
            new_answer: [],
            question_id: "",
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
            this.item = item;
            console.log(item)
            const questions: Array<Question> = Object.values(item.questions);
            this.questions = questions;
        },

        async bid() {
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

        async ask() {
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
                    const data: Question = await response.json()
                    this.questions.push(data)
                    this.new_question = ""
                }
                else {
                    window.alert("You bid was not successful");
                }
            }
            else {
                window.alert("question cannot have an empty body");
            }
        },

        async answer(question_id: string | undefined, index: number) {
            const response = await fetch(`http://localhost:8000/item/${this.$route.params.id}/${question_id}`, {
                method: 'PUT',
                credentials: "include",
                mode: "cors",
                referrerPolicy: "no-referrer",
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ answer: this.new_answer[index] }),
            });
            console.log(response.status)
            if (response.status === 200) this.questions[index].answer = this.new_answer[index]
            if (response.status === 400) alert("Cannot answer question, You are not the owner of this item")
        },
    }
}
</script>