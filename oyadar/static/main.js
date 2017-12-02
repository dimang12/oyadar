/**
 * Created by dimang12 on 10/20/17.
 */
$(function () {
    ful_height = $(window).height();
    v_height = $('.vertical-middle').height();
    $('.vertical-middle').css("top", ((ful_height/2) - (v_height/2) -40 ));

    updateDonutChart('.donut-size', 83, true);
    $('.bar-chart').each(function (k, bar) {
        data = {
          datasets:[{
              data: [31, 30,12,23],
              backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          }]
        };

        var myBarChart = new Chart(bar, {
            type: 'bar',
            data: {
                labels: ["CIS 6", "CIS 5", "Bus 1A", "Animation 200"],
                datasets: [
                    {
                        label: "Class Attendance",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9"],
                        data: [80,82,75,90]
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true,
                            max: 100
                        }
                    }]
                }

            }
        });
    });
    // var ctx = document.getElementById("myChart");
    $('.doughnut-chart').each(function (k, obj) {
        data = {
            datasets: [{
                data: [$(obj).attr("data-score"),(100 - $(obj).attr("data-score"))],
                backgroundColor: ["#1abc9c"],
                borderWidth: 3,
                responsive: true
            }],

            // These labels appear in the legend and in the tooltips when hovering different arcs
            labels: [
                'Completed',
                'Uncompleted'
            ],

        };
        var myPieChart = new Chart( obj,{
            type: 'doughnut',
            data: data,
            options: {
                legend:{
                    display: false,
                    labels: {
                        fontColor: '#00550'
                    }
                },
                title: {
                    display: true,
                    text: $(obj).attr("data-label")
                }
            }

            // options: options
        });
    });

});
