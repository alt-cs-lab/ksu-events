let coachEmailTagSelector = "#div_id_coach_email"
let isMinorTagSelector = "#div_id_is_minor"
let isCoachTagSelector = "#div_id_is_coach"

let isMinorSelector = "#id_is_minor"
let isCoachSelector = "#id_is_coach"

$(document).ready(function () {
    $('select[multiple]').multiselect({
        includeSelectAllOption: false
    });


    if($(isMinorSelector).prop('checked')) {
        $(isCoachSelector).prop('checked', false);
        $(isCoachTagSelector).addClass('d-none');
        $(coachEmailTagSelector).removeClass('d-none');
    }
    else{
        $(coachEmailTagSelector).addClass('d-none');
    }

    $(isMinorSelector).on('change', function () {
            if (this.checked) {
                $(isCoachTagSelector).addClass('d-none');
                $(isCoachSelector).prop('checked', false);
                $(coachEmailTagSelector).removeClass('d-none');
            }
            else{
                $(coachEmailTagSelector).addClass('d-none');
                $(isCoachTagSelector).removeClass('d-none');
            }
        }
    )
    $(isCoachSelector).on('change', function () {
            if (this.checked) {
                $(isMinorTagSelector).addClass('d-none');
                $(isMinorSelector).prop('checked', false);
            }
            else{
                $(isMinorTagSelector).removeClass('d-none');
            }
        }
    )
});