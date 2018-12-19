$(document).ready(function(){
	$.ajax({
        url:'api/users',
        type:'GET',
        dataType:'json',
        // contentType: "application/json",
        success:function(data){
        	console.log("返回数据：" + JSON.stringify(data));
        	// var json = {"data":[{"phone_number":"13147045012","pay_type":85,"booking_leave_date":"2018-12-15","order_type":105,"nick_name":"SHOW","price":1,"booking_checkin_date":"2018-12-14","unit_price":1,"booking_num":1,"hotel_address":"西环路","order_state":16,"order_date":"2018-12-14 17:59:01","order_number":"1000000011801","hotel_name":"优客未来酒店"},{"phone_number":"13147045012","pay_type":85,"booking_leave_date":"2018-12-15","order_type":105,"nick_name":"SHOW","price":1,"booking_checkin_date":"2018-12-14","unit_price":1,"booking_num":1,"hotel_address":"西环路","order_state":16,"order_date":"2018-12-14 17:55:27","order_number":"1000000011800","hotel_name":"优客未来酒店"},{"phone_number":"13147045012","pay_type":85,"booking_leave_date":"2018-12-15","order_type":105,"nick_name":"SHOW","price":1,"booking_checkin_date":"2018-12-14","unit_price":1,"booking_num":1,"hotel_address":"西环路","order_state":16,"order_date":"2018-12-14 17:55:26","order_number":"1000000011799","hotel_name":"优客未来酒店"},{"phone_number":"13786095840","pay_type":85,"booking_leave_date":"2018-12-14","order_type":105,"nick_name":"李lili","price":1,"booking_checkin_date":"2018-12-13","unit_price":1,"booking_num":1,"hotel_address":"锦华大厦","order_state":16,"order_date":"2018-12-13 15:42:55","order_number":"1000000011798","hotel_name":"金元芳四季酒店"},{"phone_number":"13702571354","pay_type":85,"booking_leave_date":"2018-12-14","order_type":105,"nick_name":"null5416lynX","price":238,"booking_checkin_date":"2018-12-13","unit_price":238,"booking_num":1,"hotel_address":"大浪街道华盛路128号","order_state":99,"order_date":"2018-12-13 11:41:17","order_number":"1000000011797","hotel_name":"深圳市豪云天酒店有限公司"},{"phone_number":"18658585858","pay_type":84,"booking_leave_date":"2018-12-07","order_type":105,"nick_name":"null5489TM0P","price":200,"booking_checkin_date":"2018-12-06","unit_price":200,"booking_num":1,"hotel_address":"途客中国酒店","order_state":99,"order_date":"2018-12-06 18:33:13","order_number":"1000000011796","hotel_name":"途客中国酒店"},{"phone_number":"13702571354","pay_type":84,"booking_leave_date":"2018-11-28","order_type":105,"nick_name":"null5416lynX","price":250,"booking_checkin_date":"2018-11-27","unit_price":250,"booking_num":1,"hotel_address":"大浪街道华盛路128号","order_state":99,"order_date":"2018-11-27 15:22:29","order_number":"1000000011795","hotel_name":"深圳市豪云天酒店有限公司"},{"phone_number":"18658585858","pay_type":84,"booking_leave_date":"2018-11-28","order_type":105,"nick_name":"null5489TM0P","price":200,"booking_checkin_date":"2018-11-27","unit_price":200,"booking_num":1,"hotel_address":"途客中国酒店","order_state":99,"order_date":"2018-11-27 15:07:16","order_number":"1000000011794","hotel_name":"途客中国酒店"},{"phone_number":"13702571354","pay_type":85,"booking_leave_date":"2018-11-27","order_type":105,"nick_name":"null5416lynX","price":520,"booking_checkin_date":"2018-11-26","unit_price":520,"booking_num":1,"hotel_address":"大浪街道华盛路128号","order_state":99,"order_date":"2018-11-26 14:24:22","order_number":"1000000011793","hotel_name":"深圳市豪云天酒店有限公司"},{"phone_number":"13786095840","pay_type":85,"booking_leave_date":"2018-11-22","order_type":105,"nick_name":"李lili","price":1,"booking_checkin_date":"2018-11-21","unit_price":1,"booking_num":1,"hotel_address":"锦华大厦","order_state":99,"order_date":"2018-11-21 13:24:50","order_number":"1000000011792","hotel_name":"金元芳四季酒店"}]};
        	var style = "odd";
        	$.each(data.data, function(index, value) {
        		console.log("电话号码：" + value.phone_number);
        		$(".title").after(
       							"<tr class='" + style + "'>" +
        							"<td>" + value.user_id + "</td>" +
        							"<td>" + value.user_name + "</td>" +
        							"<td>" + value.nick_name + "</td>" +
        							"<td>" + value.phone_number + "</td>" +
        							"<td>" + value.gender + "</td>" +
        							"<td>" + value.reg_date + "</td>" +




       							"</tr>")//插入语句
       			style = style == "odd" ? "dual" : "odd";
        	});
        },
        error: function (data) {
        	console.log("返回数据：" + JSON.stringify(data));
        }
    });
});