

document.addEventListener("DOMContentLoaded", () => {
    const ratings = document.querySelectorAll('.rating');

    if(ratings.length > 0) {
        initRatings();
    }

    function initRatings() {
        let ratingActive, ratingValue;

        for (let i = 0; i < ratings.length; i++) {
            const rating = ratings[i];
            initRating(rating, i == ratings.length - 1);
        }

        function initRating(rating, readonly = false) {
            initRatingVars(rating);

            setRatingActiveWidth();
            setRating(rating, readonly);
        }

        function initRatingVars(rating) {
            ratingActive = rating.querySelector('.rating__active');
            ratingValue = rating.querySelector('.rating__value');
        }

        function setRatingActiveWidth(index = ratingValue.innerHTML) {
            const MAX_VALUE = 5;
            const ratingActiveWidth = index / MAX_VALUE * 100;
            ratingActive.style.width = ratingActiveWidth + "%";
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
                        rating.value.value = i  + 1;
                        setRatingActiveWidth();
                    });
                }
            }
        }
    }
})