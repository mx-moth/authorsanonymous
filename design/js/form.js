import $ from 'jquery';

function filterByName(name) {
    return (i, f) => $(f).find('[name]').attr('name') == name;
}

export const MessageLevels = {
    INFO: 'info',
    SUCCESS: 'success',
    ERROR: 'error',
};

export class AjaxForm {
    constructor($form) {
        this.$form = $form;
        this.form = new FormHelper(this.$form, {
            prefix: this.$form.data('prefix'),
        });

        this.bind();
    }

    bind() {
        this.$form.on('submit', (e) => {
            e.preventDefault();
            this.submit();
        });
    }

    submit() {
        this.form.clearErrors();
        this.form.clearMessages();
        this.form.waiting = true;

        fetch(this.$form.attr('action'), {
            method: this.$form.attr('method'),
            body: new FormData(this.$form.get(0)),
            credentials: 'same-origin',
        }).then((response) => {
            if (response.status >= 200 && response.status < 300) {
                return this.handleSuccess(response);
            } else if (response.status == 422) {
                return this.handleFormError(response);
            } else {
                return this.handleError(response);
            }
        }).finally(() => {
            this.form.waiting = false;
        });
    }

    handleSuccess(response) {
        this.form.addMessage('You have been subscribed', MessageLevels.SUCCESS);
        this.$form.get(0).reset();
    }

    handleFormError(response) {
        return response.json()
        .then((json) => this.form.populateServerErrors(json));
    }

    handleError(response) {
        this.form.addMessage(
            'There was a problem adding you to the mailing list. Please try again.',
            MessageLevels.ERROR);
    }
}

export class FormHelper {

    constructor($form, {prefix = null} = {}) {
        this.$form = $form;
        this.prefix = prefix;
    }

    get waiting() {
        return this.$form.hasClass('waiting');
    }
    set waiting(waiting) {
        this.$form.toggleClass('waiting', waiting);
    }

    get fields() {
        return this.$form.find('.field');
    }

    getField(name) {
        console.log("Looking for field with name", name);
        return this.fields.filter(filterByName(this._prefixName(name)));
    }

    clearErrors() {
        const $fields = this.fields.filter('.has-error');
        $fields.find('.error-message').remove();
        $fields.removeClass('has-error');

        return this;
    }

    addError(name, error) {
        const $field = this.getField(name);

        $field.addClass('has-error');
        $field.append($('<p class="error-message">').text(error));

        return this;
    }

    populateServerErrors(responseJson) {
        const errors = responseJson.errors;
        Object.entries(errors).forEach(([field, errors]) => {
            errors.forEach((error) => {
                this.addError(field, error.message);
            });
        });
    }

    clearMessages() {
        this.$form.find('.message').remove();
    }

    addMessage(message, level) {
        const $wrapper = $('<div>').addClass(`message message--${level}`);
        const $text = $('<p>').text(message).appendTo($wrapper);
        this.$form.prepend($wrapper);
    }

    _prefixName(name) {
        if (this.prefix) {
            return `${this.prefix}-${name}`;
        } else {
            return name;
        }
    }

}
