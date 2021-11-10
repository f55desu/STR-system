const MAX_VALUE = 5;

function initRatings(ratingsContainerSelector) {
    const ratingsContainer = document.querySelector(ratingsContainerSelector);
    const ratings = Array.from(ratingsContainer.querySelectorAll(".rating"));

    ratings.forEach(r => initRating(r, ratings));
}

function initRating(rating, ratings) {
    initRatingVars(rating);

    const isReadonly = rating.hasAttribute("readonly");

    setRatingActiveWidth();
    setAVGRating(ratings);
    setRating(rating, isReadonly, ratings);
}

function initRatingVars(rating) {
    ratingActive = rating.querySelector('.rating__active');
    ratingValue = rating.querySelector('.rating__value');
}

function setRatingActiveWidth(index = ratingValue.innerHTML) {
    const ratingActiveWidth = index / MAX_VALUE * 100;
    ratingActive.style.width = ratingActiveWidth + "%";
}

function setAVGRating(ratings) {
    let values = [];

    ratings.forEach((r, i) => {
        const rating = r.querySelector('.rating__value');

        if (r.hasAttribute("readonly") || !r.hasAttribute("value")) 
            return;

        values.push(Number(rating.innerHTML));
    })

    const lastRatings = Array.from(ratings)
        .filter(r => r.hasAttribute("readonly"))
        .forEach(r => {
            const avg = values.reduce((a, b) => a + b, 0) / values.length;

            r.querySelector(".rating__value").innerHTML = avg;
            r.querySelector(".rating__value").value = avg;
            r.querySelector(".rating__active").style.width = `${avg / MAX_VALUE * 100}%`;
        }) 
}

function setRating(rating, readonly, ratings) {
    const ratingItems = rating.querySelectorAll('.rating__item');

    for (let i = 0; i < ratingItems.length; i++) {
        const ratingItem = ratingItems[i];

        if (!readonly) {
            ratingItem.addEventListener("mouseenter", e => {
                initRatingVars(rating);
                setRatingActiveWidth(ratingItem.value);
            });

            ratingItem.addEventListener("mouseleave", e => {
                setRatingActiveWidth(ratingValue.value);
            });

            ratingItem.addEventListener("click", e => {
                initRatingVars(rating);

                ratingValue.innerHTML = i + 1;
                ratingValue.value = i  + 1;
                setRatingActiveWidth();
                setAVGRating(ratings);
            });
        }
    }
}