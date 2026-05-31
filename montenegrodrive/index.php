<?php
/**
 * Default template (blog index / archive fallback).
 *
 * Most pages should use the Elementor canvas via the page templates,
 * but WordPress requires this file to exist.
 *
 * @package MontenegroDrive
 */

if ( ! defined( 'ABSPATH' ) ) { exit; }

get_header();
?>

<div class="max-w-container-max mx-auto px-gutter py-section-padding">

    <?php if ( have_posts() ) : ?>

        <?php if ( is_home() && ! is_front_page() ) : ?>
            <header class="mb-stack-lg">
                <h1 class="font-h1 text-h1 text-primary"><?php single_post_title(); ?></h1>
            </header>
        <?php endif; ?>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-stack-lg">
            <?php while ( have_posts() ) : the_post(); ?>
                <article id="post-<?php the_ID(); ?>" <?php post_class( 'bg-surface-container-lowest rounded-xl overflow-hidden shadow-sm hover:shadow-md transition-shadow' ); ?>>
                    <?php if ( has_post_thumbnail() ) : ?>
                        <a href="<?php the_permalink(); ?>" class="block aspect-[4/3] overflow-hidden">
                            <?php the_post_thumbnail( 'large', array( 'class' => 'w-full h-full object-cover hover:scale-105 transition-transform duration-500' ) ); ?>
                        </a>
                    <?php endif; ?>
                    <div class="p-6">
                        <h2 class="font-h3 text-h3 mb-2">
                            <a href="<?php the_permalink(); ?>" class="text-primary hover:text-primary-container"><?php the_title(); ?></a>
                        </h2>
                        <div class="text-body-sm text-secondary mb-4">
                            <?php echo esc_html( get_the_date() ); ?>
                        </div>
                        <div class="text-on-surface-variant"><?php the_excerpt(); ?></div>
                    </div>
                </article>
            <?php endwhile; ?>
        </div>

        <div class="mt-stack-lg">
            <?php
            the_posts_pagination(
                array(
                    'mid_size'  => 2,
                    'prev_text' => __( '« Previous', 'montenegrodrive' ),
                    'next_text' => __( 'Next »', 'montenegrodrive' ),
                )
            );
            ?>
        </div>

    <?php else : ?>

        <div class="text-center py-section-padding">
            <h1 class="font-h2 text-h2 text-primary mb-stack-md"><?php esc_html_e( 'Nothing here yet', 'montenegrodrive' ); ?></h1>
            <p class="text-body-lg text-secondary"><?php esc_html_e( 'Create a page in WordPress and edit it with Elementor — or import the bundled MontenegroDrive templates.', 'montenegrodrive' ); ?></p>
        </div>

    <?php endif; ?>

</div>

<?php get_footer();
