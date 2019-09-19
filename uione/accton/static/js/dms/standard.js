let initFunctionLoad = function(){
    uploadFile();
}

let getUploadInformation = function(){
    const fileUploader = document.querySelector('#file-uploader');
    fileUploader.addEventListener('change', (e) => {
    console.log(e.target.files); // get file object
    });
}

let uploadFile = function(){
    $('#upload-file-btn').click(function() {
        var form_data = new FormData($('#upload-file')[0]);
        $.ajax({
            type: 'POST',
            url: 'http://' + Config.ip_address + Config.port + '/dms/uploadFile/',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
            },
        });
    });
}

addLoadEvent(initFunctionLoad)