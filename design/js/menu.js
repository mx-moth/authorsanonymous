export class Menu {

    constructor($el, $body) {
        this.$el = $el;
        this.$body = $body;
        this.visibleClass = 'is-menu-visible';
        this.locked = false;
        this.bind();
    }

    lock() {
        if (this.locked)
            return false;

        this.locked = true;

        window.setTimeout(() => {
            this.locked = false;
        }, 350);

        return true;
    }

    show() {
        if (this.lock()) {
            this.$body.addClass(this.visibleClass);
        }
    }

    hide() {
        if (this.lock()) {
            this.$body.removeClass(this.visibleClass);
        }
    }

    toggle() {
        if (this.lock()) {
            this.$body.toggleClass(this.visibleClass);
        }
    }

    bind() {
        this.$el
            .appendTo(this.$body)
            .on('click', (event) => {
                event.stopPropagation();
                this.hide();
            });
        this.$el.find('.inner')
            .on('click', '.close', (event) => {
                event.preventDefault();
                event.stopPropagation();
                event.stopImmediatePropagation();
                this.hide();
            })
            .on('click', (event) => {
                event.stopPropagation();
            })
            .on('click', 'a', (event) => {
                var href = $(this).attr('href');
                event.stopPropagation();

                this.hide();
            });
        this.$body
            .on('click', 'a[href="#menu"]', (event) => {
                event.stopPropagation();
                event.preventDefault();
                this.toggle();
            })
            .on('keydown', (event) => {
                if (event.keyCode == 27) {
                    this.hide();
                }
            });
    }
}
