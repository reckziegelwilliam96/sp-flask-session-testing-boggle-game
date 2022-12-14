class BoggleGame {
    constructor(boardId) {

        this.score=0;
        this.words = new Set();
        this.board = $("#" + boardId)

        $(".add-word", this.board).on("submit", this.handleSubmit.bind(this));
    }

    showWord(word) {
        $(".add-word", this.board).append($("<li>", { text: word}));
    }

    showScore() {
        $(".score", this.board).text(this.score);
    }
    showMessage(msg, cls) {
        $(".msg", this.board)
            .text(msg)
            .removeClass()
            .addClass(`msg ${cls}`);
    }
    
    /* handle add-guess form submission */
    async handleSubmit(evt) {
        evt.preventDefault();
        const $word = $(".word", this.board);

        let word = $word.val();
        if (!word) return;

        if (this.words.has(word)) {
            this.showMessage(`Already found ${word}`, "err")
            return;
        }
    
        const resp = await axios.get("/check-word", { params: { word: word }});
        if (resp.data.result === "not-word") {
            this.showMessage(`${word} is not in the English language`, "err");
        } else if (resp.data.result === "not-on-board") {
            this.showMessage(`${word} is not a valid word on this board`, "err");
        } else {
            this.showWord(word);
            this.score += word.length;
            this.showScore();
            this.words.add(word);
            this.showMessage(`Added: ${word}`, "ok");
        }

        $word.val("").focus();
    }
    async scoreGame() {
        $(".add-word", this.board).hide();
        const resp = await axios.post("/post-score", { score: this.score});
        if (resp.data.brokeRecord) {
            this.showMessage(`New record: ${this.score}`, "ok");
        } else {
            this.showMessage(`Final score: ${this.score}`, "ok");
        }
    }
}




