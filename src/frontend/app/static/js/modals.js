class modalCreator {
    constructor(title, body, footer_action) {
        this.modalId = 'dynamicModal-' + Math.random().toString(36).substring(2, 15);
        this.modalStructure = $(`
        <div class="modal fade" id="${this.modalId}" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="${this.modalId}Label" aria-hidden="true">
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">${title}</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
              </div>
              <div class="modal-footer">
              </div>
            </div>
          </div>
        </div>
        `);
        // append body to modal-body
        this.modalStructure.find('.modal-body').append(body);
        // append footer to modal-footer
        this.modalStructure.find('.modal-footer').append(footer_action);
        this.modalStructure.find('.btn-close').on('click', () => {
            this.remove();
        });
    }

    show() {
        $('body').append(this.modalStructure);
        const modalElement = $('#' + this.modalId);
        modalElement.modal('show');
    }

    remove() {
        const modalElement = $('#' + this.modalId);
        modalElement.modal('hide');
        modalElement.on('hidden.bs.modal', () => {
            modalElement.remove();
        });
    }
}