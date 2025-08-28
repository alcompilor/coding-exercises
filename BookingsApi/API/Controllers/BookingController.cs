using Microsoft.AspNetCore.Mvc;
using BookingsApi.Models;
using BookingsApi.Interfaces;

namespace BookingsApi.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class BookingsController(IBookingService bookingService) : ControllerBase
    {
        private readonly IBookingService _service = bookingService;

        [HttpGet]
        public IActionResult GetAll()
        {
            return Ok(_service.GetAll());
        }

        [HttpGet("{id:int}")]
        public IActionResult GetById(int id)
        {
            var booking = _service.GetById(id);
            return booking == null ? NotFound() : Ok(booking);
        }

        [HttpPost]
        public IActionResult Create([FromBody] Booking booking)
        {
            try
            {
                var created = _service.Create(booking);
                return CreatedAtAction(nameof(GetById), new { id = created.Id }, created);
            }
            catch (InvalidOperationException error)
            {
                return Conflict(error.Message);
            }
        }

        [HttpDelete("{id:int}")]
        public IActionResult Delete(int id)
        {
            var isCanceled = _service.Cancel(id);

            if (!isCanceled)
                return NotFound();

            return NoContent();
        }
    }
}
