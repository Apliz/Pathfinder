
//The HTML this links to is /templates.html
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  /* 
  The AJAX GET request to celestrack.org should remain commented out during development to prevent
  overloading their servers during development.

  The commented out ajax is the GET call

  The currently used ajax POST was removed from the SUCCESS callback function() of the celestrack GET
  It currently uses a STUB JSON that mimics an orbital body JSON object.

  When moving from development into production, the POST should be moved back into the ajax GET callback function.

  Custom succes and error messages should be created at some point to deal with the most common basic errors.
  Currently the successMessage parameter in the success callback function returns HTML...
  */
  $("#celestrackButton").on("click", function () {
    $.ajax({
      type: "POST",
      url: "/",
      contentType: "application/json",
      data: JSON.stringify([{ "OBJECT_NAME": "ISS (ZARYA)", "OBJECT_ID": "1998-067A", "EPOCH": "2024-02-13T06:44:33.788832", "MEAN_MOTION": 15.49850622, "ECCENTRICITY": 0.0001877, "INCLINATION": 51.6401, "RA_OF_ASC_NODE": 214.3545, "ARG_OF_PERICENTER": 239.5446, "MEAN_ANOMALY": 176.5165, "EPHEMERIS_TYPE": 0, "CLASSIFICATION_TYPE": "U", "NORAD_CAT_ID": 25544, "ELEMENT_SET_NO": 999, "REV_AT_EPOCH": 43918, "BSTAR": 0.00042812, "MEAN_MOTION_DOT": 0.00023923, "MEAN_MOTION_DDOT": 0 }, { "OBJECT_NAME": "ISS DEB", "OBJECT_ID": "1998-067RZ", "EPOCH": "2024-02-12T15:46:55.079616", "MEAN_MOTION": 16.04849876, "ECCENTRICITY": 0.0004614, "INCLINATION": 51.6212, "RA_OF_ASC_NODE": 132.584, "ARG_OF_PERICENTER": 355.915, "MEAN_ANOMALY": 4.1823, "EPHEMERIS_TYPE": 0, "CLASSIFICATION_TYPE": "U", "NORAD_CAT_ID": 47853, "ELEMENT_SET_NO": 999, "REV_AT_EPOCH": 16683, "BSTAR": 0.00041452, "MEAN_MOTION_DOT": 0.00288055, "MEAN_MOTION_DDOT": 4.8549e-5 }]
      ),
      success: function (succObject, succString) {
        console.log(`celestrack.js POST to app.py completed with message -> \n${succString}!`)
      },
      error: function (errObject, errString, errThrown) {
        throw new Error(errThrown, { cause: errObject });
      }
    })
    // $.ajax({
    //   url: celesTrack,
    //   data: {
    //     GROUP: "stations",
    //     FORMAT: "JSON"
    //   },
    //   success: function (response, status) {
    //     console.log(JSON.stringify(response))
    //     $.ajax({
    //       type: "POST",
    //       url: "/",
    //       contentType: "application/json",
    //       data: JSON.stringify(response),
    //       success: function (succObject, succString) {
    //         console.log(`celestrack.js POST to app.py completed with message -> \n${succString}!`)
    //       },
    //       error: function (errObject, errString, errThrown) {
    //         throw new Error(errThrown, { cause: errObject });
    //       }
    //     })
    //   },
    //   error: function (err) {
    //     console.log(err);
    //   }
    // });
  })
});