<template>
    <div class="container">
        <div class="card mb-3">
            <div class="row g-0">

                <picture class="col-md-4"><img :src="imgUrl" alt="Image depicting the item" /></picture>

                <div class="col-md-8">
                    <div class="card-body">
                        <h1 class="card-title">{{ title }}</h1>
                        <p class="card-text">{{ description }}</p>
                        <form class="form-outline">
                            <span>
                                Current Bid:
                                <strong class="display-6">{{ current_price }}£</strong>
                            </span>
                            <input id="bid" class="form-control" style="max-width: 200px;" type="number"
                                :min="(current_price + 1)" />
                            <label for="bid">Enter £{{ current_price + 1 }} or higher</label>
                            <br />
                            <button type="submit" class="btn btn-primary btn-lg">Bid</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>



        <h2>Questions</h2>
        <ul class="list-group mb-1">
            <template v-for="item in all_questions">
                <li class="list-group-item d-flex justify-content-between align-items-start">
                    <div class="ms-2 me-auto">
                        <div class="fw-bold">{{ item.question }}</div>
                        <div v-if="item.answer !== ''">{{ item.answer }}</div>
                        <div v-else>
                            <form class="form-outline">
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
        <form class="form-outline">
            <div class="form-floating">
                <input type="email" class="form-control" id="askQuestion">
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
            title: "Heavy Gold bar",
            imgUrl: "https://picsum.photos/300/500",
            description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam posuere finibus lectus sit amet dignissim. Sed malesuada blandit dictum. Mauris vitae metus eros. Quisque eleifend, dui id tempus bibendum, leo ipsum porttitor nisi, sed blandit lorem ex eu libero. Donec eu massa libero.",
            current_price: 34,
            all_questions: [{ question: "how are you?", answer: "Good and you?" }, { question: "Is the gold yellow?", answer: "Yes?" }, { question: "Is the gold yellow?", answer: "" }, { question: "Is the gold yellow?", answer: "Yes?" }],
        }
    }
}
</script>