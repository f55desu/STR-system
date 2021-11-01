

document.addEventListener("DOMContentLoaded", () => {
    const ratings = document.querySelectorAll('.rating');

    if(ratings.length > 0) {
        initRatings();
    }

    function initRatings() {
        let ratingActive, ratingValue;
        const MAX_VALUE = 5;

        for (let i = 0; i < ratings.length; i++) {
            const rating = ratings[i];
            initRating(rating, i == ratings.length - 1);
        }

        function initRating(rating, readonly = false) {
            initRatingVars(rating);

            setRatingActiveWidth();
            setAVGRating();
            setRating(rating, readonly);
        }

        function initRatingVars(rating) {
            ratingActive = rating.querySelector('.rating__active');
            ratingValue = rating.querySelector('.rating__value');
        }

        function setRatingActiveWidth(index = ratingValue.innerHTML) {
            const ratingActiveWidth = index / MAX_VALUE * 100;
            ratingActive.style.width = ratingActiveWidth + "%";
        }

        function setAVGRating() {
            let values = [];

            ratings.forEach((r, i) => {
                const rating = r.querySelector('.rating__value');
                if (i === ratings.length - 1) return;
                values.push(Number(rating.innerHTML));
            })

            const lastRating = ratings[ratings.length - 1];
            const avg = values.reduce((a, b) => a + b, 0) / values.length;

            lastRating.querySelector(".rating__value").innerHTML = avg;
            lastRating.querySelector(".rating__value").value = avg;
            lastRating.querySelector(".rating__active").style.width = `${avg / MAX_VALUE * 100}%`;
        }
        
        function setRating(rating, readonly) {
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
                        setAVGRating();
                    });
                }
            }
        }
    }
})