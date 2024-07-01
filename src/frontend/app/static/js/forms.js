class DynamicForm {
    constructor(data, options = {}) {
        this.data = data;
        this.nonEditableFields = options.nonEditableFields || [];
        this.excludeFields = options.excludeFields || [];
        this.dropdownFields = options.dropdownFields || {};
        this.requiredFields = options.requiredFields || [];
    }

    createForm(submitText, onSubmit) {
        const form = document.createElement('form');
        form.classList.add('needs-validation');
        form.noValidate = true;

        Object.keys(this.data).forEach(field => {
            if (!this.excludeFields.includes(field)) {
                const formGroup = document.createElement('div');
                formGroup.classList.add('mb-3');

                const label = document.createElement('label');
                label.classList.add('form-label');
                label.setAttribute('for', field);
                label.innerText = this.capitalizeFirstLetter(field);
                formGroup.appendChild(label);

                let input;
                if (this.dropdownFields[field]) {
                    input = this.createDropdown(field);
                } else {
                    input = document.createElement('input');
                    input.type = 'text';
                    input.classList.add('form-control');
                    input.value = this.data[field];
                }

                input.name = field;
                input.id = field;
                if (this.nonEditableFields.includes(field)) {
                    input.setAttribute('readonly', 'readonly');
                    input.setAttribute('disabled', 'disabled');
                    input.classList.add('form-control-plaintext');
                }

                if (this.requiredFields.includes(field)) {
                    input.setAttribute('required', 'required');
                }

                formGroup.appendChild(input);
                form.appendChild(formGroup);
            }
        });

        const submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.classList.add('btn', 'btn-primary', 'float-end');
        submitButton.innerText = submitText || 'Submit'; // Set text for submit button

        submitButton.addEventListener('click', event => {
            event.preventDefault(); // Prevent default form submission behavior

            if (form.checkValidity()) {
                const formData = this.getFormData();
                onSubmit(formData); // Call the onSubmit function with form data
            } else {
                form.classList.add('was-validated');
            }
        });

        form.appendChild(submitButton);

        return form;
    }

    createDropdown(field) {
        const select = document.createElement('select');
        select.classList.add('form-select');

        this.dropdownFields[field].forEach(option => {
            const optionElement = document.createElement('option');
            optionElement.value = option;
            optionElement.innerText = option;
            select.appendChild(optionElement);
        });

        if (this.requiredFields.includes(field)) {
            select.setAttribute('required', 'required');
        }

        return select;
    }

    getFormData() {
        const formData = {};
        document.querySelectorAll('form input, form select').forEach(input => {
            if (!this.excludeFields.includes(input.name)) {
                formData[input.name] = input.value;
            }
        });
        return formData;
    }

    capitalizeFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }
}
