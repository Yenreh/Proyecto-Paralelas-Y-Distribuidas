class AjaxHelper {
    static get(url, callback, errorCallback) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url);
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    callback(xhr.responseText);
                } else {
                    if (errorCallback) {
                        errorCallback(xhr.status);
                    }
                }
            }
        };
        xhr.send();
    }

    static post(url, data, callback, errorCallback) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', url);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function () {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    callback(xhr.responseText);
                } else {
                    if (errorCallback) {
                        errorCallback(xhr.status);
                    }
                }
            }
        };
        xhr.send(JSON.stringify(data));
    }
}
