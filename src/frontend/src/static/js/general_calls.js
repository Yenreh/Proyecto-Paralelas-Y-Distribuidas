class AjaxHelper {
    static get(url, callback, errorCallback) {
        $.ajax({
            url: url,
            type: 'GET',
            async: false,
            success: function(response) {
                callback(response);
            },
            error: function(xhr, status, error) {
                if (errorCallback) {
                    errorCallback(xhr.status);
                }
            }
        });
    }

    static post(url, data, callback, errorCallback) {
        $.ajax({
            url: url,
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                callback(response);
            },
            error: function(xhr, status, error) {
                if (errorCallback) {
                    errorCallback(xhr.status);
                }
            }
        });
    }
    static put(url, data, callback, errorCallback) {
        $.ajax({
            url: url,
            type: 'PUT',
            contentType: 'application/json',
            data: JSON.stringify(data),
            success: function(response) {
                callback(response);
            },
            error: function(xhr, status, error) {
                if (errorCallback) {
                    errorCallback(xhr.status);
                }
            }
        });
    }

    static delete(url, callback, errorCallback) {
        $.ajax({
            url: url,
            type: 'DELETE',
            success: function(response) {
                callback(response);
            },
            error: function(xhr, status, error) {
                if (errorCallback) {
                    errorCallback(xhr.status);
                }
            }
        });
    }
}
